"""
This module provides a class, EmailSender, for sending emails using the SMTP protocol.
The class supports various email operations such as composing and sending emails with optional attachments.

Classes:
    EmailSender: Encapsulates methods for connecting to an SMTP server, composing emails, and sending them.

The EmailSender class includes the following methods:
    - send_email: Composes and sends an email to specified recipients with optional attachments.
    - _get_connection: Establishes and returns a connection to the SMTP server.
    - _compose_email: Creates an email message with the specified subject, recipients, content, and attachments.
    - _attach_file: Attaches a file to the email message.

Usage:
    To use this module, create an instance of EmailSender with the SMTP server details and the environment variable name holding the password.
    Then, call the send_email method to send an email with the desired content and attachments.
"""

import os
import smtplib
from email.message import EmailMessage


class EmailSender:
    def __init__(self, user: str, password_env_var: str, smtp_server: str = 'smtp.office365.com', smtp_port: int = 587):
        self.user = user
        self.password = os.getenv(password_env_var)
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject: str, recipients: str | list[str], content: str, content_type: str = 'plain',
                   attachments: str | None = None):
        """
        Send an email with the specified subject, recipients, and content

        Args:
            subject (str): The subject of the email.
            recipients (str | list[str]): A single recipient or a list of recipients.
            content (str): The content of the email.
            content_type (str, optional): The MIME type of the email content ('plain' or 'html'). Defaults to 'plain'.
            attachments (str | None, optional): A list of file paths to attach to the email. Defaults to None.

        Raises:
            Exception: If there is any issue in composing or sending the email.
        """
        try:
            msg = self._compose_email(subject, recipients, content, content_type, attachments)

            with self._get_connection() as smtp:
                smtp.send_message(msg)
        except Exception:
            raise

    def _get_connection(self):
        """Establish and return a connection to the SMTP server."""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.user, self.password)
            return server
        except Exception:
            raise

    def _compose_email(self, subject, recipients, content, content_type='plain', attachments=None):
        """Compose an email message with the specified details."""
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.user

        # Add recipient(s)
        if isinstance(recipients, list):
            recipients = list(filter(None, recipients))
            msg['Bcc'] = ', '.join(recipients)
        else:
            msg['Bcc'] = recipients
        msg.set_content(content, subtype=content_type)

        # Add attachment(s)
        if attachments:
            for file_path in attachments:
                self._attach_file(msg, file_path)

        return msg

    def _attach_file(self, msg, file_path):
        """Attach a file to the email message."""
        try:
            with open(file_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        except Exception:
            raise
