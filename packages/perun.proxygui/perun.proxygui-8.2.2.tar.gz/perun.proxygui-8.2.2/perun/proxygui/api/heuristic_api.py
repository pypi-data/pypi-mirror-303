import socket
from ipaddress import ip_address, ip_network

from perun.utils.auth_event_loggig.AuthEventLoggingDbModels import (
    AuthEventLoggingTable,
    UserAgentTable,
    UserAgentRawTable,
    RequestedAcrsTable,
    LoggingSpTable,
    LoggingIdpTable,
    UpstreamAcrsTable,
    SessionIdTable,
)
from sqlalchemy import create_engine, MetaData, select
from user_agents import parse
from socket import getnameinfo
import json


# Queries for fetching data from AuthEventMicroService
class AuthEventLoggingQueries:
    def __init__(self, cfg):
        # Vars for storing arrays with DB responses
        self.auth_result = None  # Auth data, Upstream, Requested and Services
        self.raw_user_agents = None  # User agents and upstream logs
        self.time_result = None  # Many AuthEvent logs
        # Nunbers of retrieved rows from DB for various data
        self.few_time_logs = cfg["heuristic_page"]["few_time_logs"]
        self.some_time_logs = cfg["heuristic_page"]["some_time_logs"]
        self.many_time_logs = cfg["heuristic_page"]["many_time_logs"]
        # DB connect string
        self.logging_db = cfg["heuristic_page"]["auth_event_logging"]["logging_db"]
        # REFEDS profile for MFA.
        self.REFEDS_MFA = "https://refeds.org/profile/mfa"
        # Microsoft authentication context for MFA.
        self.MS_MFA = "http://schemas.microsoft.com/claims/multipleauthn"
        # Contexts trusted as multifactor authentication, in the order of
        # preference (for replies).
        self.MFA_CONTEXTS = [self.REFEDS_MFA, self.MS_MFA]
        # Answers to be displayed in UI
        self.REQUEST_MFA_VALUE = {
            "required": "MFA required",
            "preferred": "MFA preferred",
            "other": "Other auth.",
        }
        self.tables = [
            AuthEventLoggingTable.__table__,
            UserAgentTable.__table__,
            UserAgentRawTable.__table__,
            RequestedAcrsTable.__table__,
            LoggingSpTable.__table__,
            LoggingIdpTable.__table__,
            UpstreamAcrsTable.__table__,
            SessionIdTable.__table__,
        ]
        self.private_ip_segments = cfg["heuristic_page"].get("private_ip_segments", [])

    # Modify ACRs value from string to list
    # '["acr1","acr2"]' -> ['acr1', 'acr2']
    # "acr1" -> ['acr1']
    def strip_acrs(self, acr):
        listed_acrs = acr.strip("][").split(",")
        for i, item in enumerate(listed_acrs):
            listed_acrs[i] = item.strip(" ").strip('"')
        return listed_acrs

    # Simple function for return type of requested authentication
    def requested_acr_status(self, raw_acr, local_mfa_performed):
        if local_mfa_performed:
            return self.REQUEST_MFA_VALUE["required"]

        acr = self.strip_acrs(raw_acr)
        if not acr:
            return self.REQUEST_MFA_VALUE["other"]
        elif len(set(acr) - set(self.MFA_CONTEXTS)) == 0:
            return self.REQUEST_MFA_VALUE["required"]
        elif acr[0] in self.MFA_CONTEXTS:
            return self.REQUEST_MFA_VALUE["preferred"]
        else:
            return self.REQUEST_MFA_VALUE["other"]

    # Basic checker if MFA was performed based on upstream_acrs value
    def upstream_acr_status(self, acr):
        if not acr:
            return None
        mfa_status = next((mfa for mfa in self.MFA_CONTEXTS if mfa in acr), None)
        return mfa_status is not None

    # Return specific number of logs from main table
    # Also joined in some requests
    def get_auth_logs(self, user_id):
        engine = create_engine(self.logging_db)
        with engine.begin() as cnxn:
            meta_data = MetaData()
            meta_data.reflect(engine)

            # Create all if not exists
            meta_data.create_all(cnxn, self.tables, checkfirst=True)

            auth_table = AuthEventLoggingTable().__table__
            agents_raw_table = UserAgentRawTable().__table__
            upstream_table = UpstreamAcrsTable().__table__
            requested_table = RequestedAcrsTable().__table__
            services_table = LoggingSpTable().__table__

            # Returns last 'self.short_time_logs' logs
            # for specific user, sorted
            # by descending time joined with upstream ACRs, requested ACRs
            # and services table

            inner_query = (
                select(
                    auth_table.c.day.label("day"),
                    auth_table.c.geolocation_city.label("geolocation_city"),
                    auth_table.c.geolocation_country.label("geolocation_country"),
                    auth_table.c.local_mfa_performed.label("local_mfa_performed"),
                    auth_table.c.ip_address.label("ip_address"),
                    requested_table.c.value.label("requested_value"),
                    upstream_table.c.value.label("upstream_value"),
                    services_table.c.name.label("name"),
                    services_table.c.identifier.label("identifier"),
                )
                .select_from(auth_table)
                .join(
                    requested_table,
                    requested_table.c.id == auth_table.c.requested_acrs_id,
                    isouter=True,
                )
                .join(
                    upstream_table,
                    upstream_table.c.id == auth_table.c.upstream_acrs_id,
                    isouter=True,
                )
                .join(
                    services_table,
                    services_table.c.id == auth_table.c.sp_id,
                    isouter=True,
                )
                .where(auth_table.c.user_id == user_id)
                .distinct(auth_table.c.ip_address)
            ).alias("inner_query")

            # Inner query allows to select distinct IPs and order by dates at the same time
            outer_query = (
                select(
                    inner_query.c.day,
                    inner_query.c.geolocation_city,
                    inner_query.c.geolocation_country,
                    inner_query.c.local_mfa_performed,
                    inner_query.c.ip_address,
                    inner_query.c.requested_value,
                    inner_query.c.upstream_value,
                    inner_query.c.name,
                    inner_query.c.identifier,
                )
                .select_from(inner_query)
                .order_by(inner_query.c.day.desc())
            )

            response = cnxn.execute(outer_query).fetchall()
            self.auth_result = [r._asdict() for r in response]

            # Return last 'self.long_time_logs' logs
            # for user, sorted by time for logging graph
            query = (
                auth_table.select()
                .order_by(auth_table.c.day.desc())
                .where(auth_table.c.user_id == user_id)
                .limit(self.many_time_logs)
            )
            response = cnxn.execute(query).fetchall()
            self.time_result = [r._asdict() for r in response]

            # Returns joined values from user_agents and upstream_acrs
            # joined on auth_event_logging table
            query = (
                select(
                    agents_raw_table.c.value.label("agent_value"),
                    upstream_table.c.value.label("upstream_value"),
                    auth_table.c.local_mfa_performed.label("local_mfa_performed"),
                )
                .select_from(auth_table)
                .join(
                    agents_raw_table,
                    agents_raw_table.c.id == auth_table.c.user_agent_id,
                    isouter=True,
                )
                .join(
                    upstream_table,
                    upstream_table.c.id == auth_table.c.upstream_acrs_id,
                    isouter=True,
                )
                .where(auth_table.c.user_id == user_id)
                .order_by(auth_table.c.day.desc())
                .limit(self.some_time_logs)
            )
            response = cnxn.execute(query).fetchall()
            # Returned dictionary:
            # {"agents_value": "val", "upstream_value": "val"}
            self.raw_user_agents = [r._asdict() for r in response]

    # ----------------- Retrieving methods --------------
    # Get information about last n cities (city name, timestamp, MFA performed status)
    def get_last_n_cities(self):
        if self.auth_result is None:
            return []

        cities = []

        # Retrieve relevant data from results
        for item in self.auth_result:
            city = item["geolocation_city"] or "Unknown city"
            country = item["geolocation_country"] or "Unknown country"
            time = item["day"].strftime("%d. %m. %Y %H:%M")
            value = city + ", " + country + " (" + time + ")"

            cities.append(
                {
                    "value": value,
                    "mfa": self.upstream_acr_status(item["upstream_value"])
                    or item["local_mfa_performed"],
                }
            )

        return cities

    # Retrieve information about last n IP addresses connected from
    # (IP address, hostname lookup, MFA performed)
    def get_last_n_ips(self):
        if self.auth_result is None:
            return []

        ips = []
        for item in self.auth_result:
            ip = item["ip_address"]
            try:
                ip_lookup = getnameinfo((ip, 0), 0)[0]
            except socket.gaierror:
                ip_lookup = ""
            ip_string = (
                ip
                if (ip == ip_lookup or ip_lookup == "")
                else ip + " (" + ip_lookup + ")"
            )

            private_ip_range_name = ""
            for private_ip_range, range_name in self.private_ip_segments.items():
                if ip_address(ip) in ip_network(private_ip_range):
                    private_ip_range_name = range_name
                    break

            if private_ip_range_name:
                value = f"{ip_string}, {private_ip_range_name}"
            else:
                city = item["geolocation_city"] or "Unknown city"
                country = item["geolocation_country"] or "Unknown country"
                value = f"{ip_string}, {city}, {country}"

            ips.append(
                {
                    "value": value,
                    "mfa": self.upstream_acr_status(item["upstream_value"])
                    or item["local_mfa_performed"],
                }
            )

        return ips

    # Retrive time statisctic from last n logs in AuthLogging table
    # retrun list in format to show Javascript graph [{"label": "8:00","value": 4},...]
    def get_last_n_times(self):
        if self.time_result is None:
            return []

        # Prefill labels - showing even empty colums
        times = [
            {
                "label": str(i) + ":00",
                "value": sum(1 for item in self.time_result if item["day"].hour == i),
            }
            for i in range(1, 25)
        ]
        return json.dumps(times)

    # Retrieve data of used user agents - compress same user agent and sort them by
    # usage, MFA performed is True if it was performed at least once on that
    # specific user agent
    def get_unique_user_agents(self):
        if self.raw_user_agents is None:
            return []

        agents = []

        for item in self.raw_user_agents:
            # Create default dictionary
            mfa_performed = (
                self.upstream_acr_status(item["upstream_value"])
                or item["local_mfa_performed"]
            )
            parsed_agent = str(parse(item["agent_value"]))

            index = next(
                (i for i, item in enumerate(agents) if item["label"] == parsed_agent),
                None,
            )
            if index is None:  # NEW User agent
                agents.append(
                    {
                        "label": parsed_agent,
                        "value": 1,
                        "mfa": mfa_performed,
                    }
                )
            else:  # Already existing user agent, only update the data
                agents[index]["value"] += 1
                agents[index]["mfa"] |= mfa_performed

        sorted_agents = sorted(agents, key=lambda d: d["value"], reverse=True)

        return sorted_agents

    # Retrieve data of used services, their name and identifier
    # Also with type of requested ACRs and upstream ACRs
    def get_last_n_services(self):
        if self.auth_result is None:
            return []

        services = []

        for item in self.auth_result:
            requested_acrs = self.requested_acr_status(
                item["requested_value"], item["local_mfa_performed"]
            )
            upstream_acrs = self.upstream_acr_status(item["upstream_value"])
            services.append(
                {
                    "name": item["name"],
                    "identifier": item["identifier"],
                    "requested_acrs": requested_acrs,
                    "upstream_acrs": upstream_acrs,
                    "local_mfa_performed": item["local_mfa_performed"],
                }
            )
        return services
