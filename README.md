
# Python Google API Challenge

## Task

- setup a test gmail account and enable the APIs for it
- cover the following features:
    - send emails
    - search for specific messages in the mailbox, e.g. for keywords in subject or body text
- a brief documentation of your steps in terms what is needed to setup this API connection, PLEASE in your words not just copy & paste from google


## Tech Stack

- Python 3.9.0
- Gmail API - Google :https://developers.google.com/gmail/api 


## Setup API

    1. Login to Google Cloud console - https://console.cloud.google.com/
    2. Setup Gmail API -  https://developers.google.com/gmail/api/guides 
    3. Generate OAuth 2.0 Client IDs and Download keep in folder tokens\client_secrets.json
    4. Also Add http://localhost:56390/ in Authorised redirect URI's while creating OAuth 2.0 Client IDs
    5. Done


## Run Locally

Clone the project

```bash
  git clone https://github.com/karanjagad/google_api_usage.git
```

Go to the project directory

```bash
  cd google_api_usage
```

Create Virtual Environment 

```bash
  python -m venv venv
```
or
```bash
  python3 -m venv venv
```
Activate the Virtual Environment for Mac and Linux

```bash
  source .venv\bin\activate
```
Activate the Virtual Environment for Windows

```bash
  .venv\Scripts\activate.bat
```
Install Requirements

```bash
  pip install -r requirements.txt
```

Run the program

```bash
  python main.py
```

