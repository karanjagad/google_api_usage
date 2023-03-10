import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText


class GmailAPI:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.scope = [
            "https://www.googleapis.com/auth/gmail.readonly",
            "https://www.googleapis.com/auth/gmail.send",
        ]
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        creds = self.creds
        token_path = os.path.join("tokens", "tokens.json")
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, self.scope)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, self.scope
                )
                creds = flow.run_local_server(port=56390)
            # Save the credentials for the next run
            with open(token_path, "w") as token:
                token.write(creds.to_json())
        self.service = build("gmail", "v1", credentials=creds)

    def send_email(self, recipient, subject, body):
        message = MIMEText(body)
        message["to"] = recipient
        message["subject"] = subject
        create_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (
                self.service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            response = f'sent message to {message} Message Id: {message["id"]}'

        except HttpError as error:
            response = f"An error occurred: {error}"
            message = None

        return response

    def search_messages(self, query):
        try:
            result = (
                self.service.users().messages().list(userId="me", q=query).execute()
            )
            messages = result.get("messages")
            if not messages:
                print("No messages found.")
                return None
            else:
                print(f"Total messages found: {len(messages)}")
                return messages
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None


if __name__ == "__main__":
    # Initializing
    credentials_path = os.path.join("tokens", "client_secret.json")
    gmail_api = GmailAPI(credentials_path)

    # Sending a Test Mail to the recipant account
    recipient = "karanjagad@gmail.com"
    subject = "Test Email"
    body = "Hello World!"
    # Calling the send mail function which invokes the api and send the mail
    gmail_api.send_email(recipient, subject, body)

    # Search for specific messages in the mailbox, e.g. for keywords in subject or body text
    query = "subject:Test Email"
    messages = gmail_api.search_messages(query)
    if messages:
        for message in messages:
            msg = (
                gmail_api.service.users()
                .messages()
                .get(userId="me", id=message["id"])
                .execute()
            )
            print(f"Snippet: {msg['snippet']}")
