from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AuthEventLoggingTable(Base):
    __tablename__ = "auth_event_logging"

    id = Column(Integer, primary_key=True)
    day = Column(TIMESTAMP)
    user = Column(String)
    user_id = Column(Integer)
    idp_id = Column(Integer, ForeignKey("logging_idp.id"))
    sp_id = Column(Integer, ForeignKey("logging_sp.id"))
    ip_address = Column(String)
    geolocation_city = Column(String)
    geolocation_country = Column(String)
    local_mfa_performed = Column(Boolean, default=False)
    session_id = Column(Integer, ForeignKey("session_id_values.id"))
    requested_acrs_id = Column(Integer, ForeignKey("requested_acrs_values.id"))
    upstream_acrs_id = Column(Integer, ForeignKey("upstream_acrs_values.id"))
    user_agent_raw_id = Column(Integer, ForeignKey("user_agent_raw_values.id"))
    user_agent_id = Column(Integer, ForeignKey("user_agent_values.id"))


class LoggingIdpTable(Base):
    __tablename__ = "logging_idp"

    id = Column(Integer, primary_key=True)
    identifier = Column(String, unique=True)
    name = Column(String)


class LoggingSpTable(Base):
    __tablename__ = "logging_sp"

    id = Column(Integer, primary_key=True)
    identifier = Column(String, unique=True)
    name = Column(String)


class SessionIdTable(Base):
    __tablename__ = "session_id_values"

    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)


class RequestedAcrsTable(Base):
    __tablename__ = "requested_acrs_values"

    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)


class UpstreamAcrsTable(Base):
    __tablename__ = "upstream_acrs_values"

    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)


class UserAgentRawTable(Base):
    __tablename__ = "user_agent_raw_values"

    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)


class UserAgentTable(Base):
    __tablename__ = "user_agent_values"

    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)
