import os
import uuid
import smtplib
import threading
from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.encoders import encode_base64


class SMTPClient:
    def __init__(self, host: str, port: int, system_name: str, system_mail: str = None, system_password: str = None,
                 ssl: bool = True, threaded: bool = True):
        self.host = host
        self.port = port
        self.ssl = ssl
        self.system_name = system_name
        self.system_mail = system_mail
        self.system_password = system_password
        self.threaded = threaded

    def _send(self, receiver: str, content: MIMEMultipart, email, password):
        smtp_server = (self.host, self.port)
        smtp_credentials = (email, password)

        client = smtplib.SMTP_SSL if self.ssl else smtplib.SMTP
        with client(*smtp_server) as server_conn:
            server_conn.login(*smtp_credentials)
            server_conn.sendmail(
                email, receiver, content.as_string()
            )

    @staticmethod
    def _attach(email_content, attachments):
        for attachment in attachments:
            if isinstance(attachment, str):
                mime = attachment.split(".").pop()
                filename = os.path.basename(attachment)
                with open(attachment, "rb") as fp:
                    data = fp.read()
            else:
                mime = "octet-stream"
                filename = str(uuid.uuid4())
                data = attachment

            attachment_part = MIMEBase("application", mime)
            attachment_part.set_payload(data)
            encode_base64(attachment_part)
            attachment_part.add_header("Content-Transfer-Encoding", "base64")
            attachment_part.add_header("Content-Disposition", "attachment", filename=filename)
            email_content.attach(attachment_part)

    def send(self, recipient: str or list[str], content: str or MIMEMultipart, subject: str = None,
             attachments: list[str or bytes] = None, as_html: bool = True, email: str = None, password: str = None):
        if type(content) is str:
            email_content = MIMEMultipart("alternative")
            email_content.attach(MIMEText(content, "html" if as_html else "plain"))
        else:
            email_content = content

        recipients = recipient if isinstance(recipient, list) else [recipient]
        email = email or self.system_mail
        password = password or self.system_password

        if email_content.get("Subject") is None and subject is not None:
            email_content["Subject"] = subject
        if email_content.get("From") is None:
            email_content["From"] = f"{self.system_name} <{email}>"

        if attachments is not None:
            self._attach(email_content, attachments)

        assert email is not None, f"Email address is required for {self.__class__.__name__}"
        assert password is not None, f"Password is required for {self.__class__.__name__}"

        for recipient in recipients:
            email_content["To"] = recipient

            if self.threaded:
                threading.Thread(target=self._send, args=(recipient, email_content, email, password,)).start()
            else:
                self._send(recipient, email_content, email, password)
