import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
from smail import sign_message
from flask import url_for

from perun.proxygui.jwt import SingletonJWTServiceProvider
from perun.utils.Notification import NotificationType


class EmailService:
    def __init__(self, cfg):
        self.__SMTP_SERVER = cfg["mfa_reset"]["smtp_server"]
        self.__SMTP_PORT = cfg["mfa_reset"]["smtp_port"]
        self.__CERT_FILE = cfg["mfa_reset"]["cert_filepath"]
        self.__HELPDESK_EMAIL = cfg["mfa_reset"]["helpdesk_mail"]
        self.__PRIVATE_KEY = cfg["mfa_reset"]["private_key_filepath"]
        self.__TRANSLATIONS = (
            cfg["mfa_reset"].get("mfa_reset_translations", {}).get("sections")
        )
        self.__JWT_SERVICE = SingletonJWTServiceProvider.get_provider().get_service()
        self.__LOGIN_EMAIL = None
        self.__LOGIN_PASS = None

        credentials_path = cfg.get("mfa_reset", {}).get(
            "mail_login_credentials_filepath"
        )
        if credentials_path and os.path.exists(credentials_path):
            with open(credentials_path, "r") as credentials:
                self.__LOGIN_EMAIL, self.__LOGIN_PASS = credentials.read().split("\n")

    def __send_email_message(self, message: MIMEMultipart) -> None:
        with smtplib.SMTP(self.__SMTP_SERVER, self.__SMTP_PORT) as smtp_server:
            if self.__LOGIN_EMAIL and self.__LOGIN_PASS:
                smtp_server.login(self.__LOGIN_EMAIL, self.__LOGIN_PASS)
            smtp_server.send_message(message)

    def __send_signed_email_message(self, message: MIMEMultipart) -> None:
        signed_message = sign_message(message, self.__PRIVATE_KEY, self.__CERT_FILE)

        self.__send_email_message(signed_message)

    def send_mfa_reset_link(
        self, recipient_id: str, recipient_email: str, locale: str
    ) -> None:
        if not self.__TRANSLATIONS:
            return None

        message = MIMEMultipart("related")
        message["From"] = self.__LOGIN_EMAIL
        message["Subject"] = self.__TRANSLATIONS[locale]["reset_link_email_subject"]
        message["To"] = recipient_email
        jwt = self.__JWT_SERVICE.get_jwt(
            {"requester_id": recipient_id, "requester_email": recipient_email}
        )
        link = url_for("gui.mfa_reset_verify", mfa_reset_jwt=jwt, _external=True)

        message_content = (
            self.__TRANSLATIONS[locale]["reset_link_email_content"] + f" {link}"
        )

        message.attach(MIMEText(message_content, "plain", _charset="UTF-8"))

        self.__send_signed_email_message(message)

    def send_mfa_reset_notification(
        self, recipient_emails: List[str], locale: str, notif_type: NotificationType
    ) -> None:
        if not self.__TRANSLATIONS:
            return None

        message = MIMEMultipart("related")
        message["From"] = self.__LOGIN_EMAIL
        message["To"] = ", ".join(recipient_emails)

        if notif_type == NotificationType.VERIFICATION:
            message["Subject"] = self.__TRANSLATIONS[locale][
                "reset_notification_email_subject"
            ]
            message_content = self.__TRANSLATIONS[locale][
                "reset_notification_email_content"
            ]
        elif notif_type == NotificationType.CONFIRMATION:
            message["Subject"] = self.__TRANSLATIONS[locale][
                "reset_confirmation_email_subject"
            ]
            message_content = self.__TRANSLATIONS[locale][
                "reset_confirmation_email_content"
            ]
        else:
            raise Exception("Unknown notification type: " + notif_type.name)

        message.attach(MIMEText(message_content, "plain", _charset="UTF-8"))

        self.__send_signed_email_message(message)

    def send_mfa_reset_request(self, requester_id: str, requester_email: str) -> None:
        if not self.__TRANSLATIONS:
            return None

        message = MIMEMultipart("related")
        message["From"] = self.__LOGIN_EMAIL
        message["Subject"] = "MFA reset request"
        message["To"] = self.__HELPDESK_EMAIL
        message_content = (
            f"Partly verified user with ID {requester_id} and email '"
            f"{requester_email}' has requested a reset of "
            f"their Multi-Factor Authentication."
        )

        message.attach(MIMEText(message_content, "plain", _charset="UTF-8"))

        self.__send_signed_email_message(message)
