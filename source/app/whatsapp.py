import requests

ULTRAMSG_INSTANCE_ID = "your_instanceid"
ULTRAMSG_TOKEN = "your_token"

def send_whatsapp_message(phone_number, message):
    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"

    payload = {
        "token": ULTRAMSG_TOKEN,
        "to": phone_number,
        "body": message
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()
