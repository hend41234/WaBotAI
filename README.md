# <p align="center">WaBotAI
## <p align="center">WaBotAI is an AI-based WhatsApp Bot that leverages Twilio and OpenAI services to deliver intelligent responses.

**Description:**
WaBotAI is designed to enhance your WhatsApp messaging experience by incorporating artificial intelligence for intelligent and context-aware responses.

## 1. TWILIO Account Setup

Get started by registering for a free Twilio account at [Twilio](https://www.twilio.com/try-twilio). Obtain your `Account SID` and `Auth Token` from the [Twilio Console](https://www.twilio.com/console).

* **Account SID and Auth Token Configuration:**
    Open the file `app/api/message/get_message.py` in your code editor.
    Locate the variables `account_sid` and `auth_token` and replace `'YOUR_ACCOUNT_SID'` and `'YOUR_AUTH_TOKEN'` with your Twilio account SID and auth token.

    ```python
    from app.api.message.create_message import CreateMessage
    from twilio.rest import Client
    import time
    import json

    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    class GetMessage:
    ```

## 2. OPENAI Account Setup

If you don't have an OpenAI account, register at [OpenAI Platform](https://platform.openai.com/login?launch). Obtain your `API Key` from the [API Keys section](https://platform.openai.com/api-keys).

* **API Key Configuration:**
    Open the file `app/api/gpt/gpt.py` in your code editor.
    Locate the variable `api_key` and replace `'YOUR_API_KEY'` with your OpenAI API key.

    ```python
    import os
    from openai import OpenAI

    api_key = "YOUR_API_KEY"

    client = OpenAI(api_key=api_key)

    def gpt(message):
    ```

## 3. Setting Up Ngrok Server

* **Installation:**
    - Install Ngrok via Apt:

    ```bash
    $ curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
    ```

    - Install Ngrok via Snap:

    ```bash
    $ snap install ngrok
    ```

* **Auth Token:**
    ```bash
    $ ngrok config add-authtoken <token>
    ```
    If you don't have an auth token, sign up [here](https://dashboard.ngrok.com/signup) and obtain the token from [Ngrok Dashboard](https://dashboard.ngrok.com/api).

## 4. Tunneling

* **Installing Requirements:**
    Run:

    ```bash
    pip install -r requirements.txt
    ```

* **Setting up Twilio Webhook:**
    Obtain the Ngrok domain from [Ngrok Dashboard](https://dashboard.ngrok.com/cloud-edge/domains) (`this is your server`). Update the Twilio sandbox settings to use the Ngrok domain.

    ```plaintext
    e.g., https://your-server.com/api/wa
    ```
    Don't forget to add `/api/wa`.

* **Running Ngrok:**
    ```bash
    ngrok http --domain=your-domain.ngrok-free.app 8000
    ```
    Skip this step if you're using your own server.

* **Running the Application:**
    ```bash
    python main.py
    ```
## Contributing

Contributions to WaBotAI are welcome! Feel free to open issues, submit pull requests, or improve the documentation. Together, we can make WaBotAI even better.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
