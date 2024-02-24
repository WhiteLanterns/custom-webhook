import requests


def send_message(url, message):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url=url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message with status code {response.status_code}")


message = "Hello world!"
send_message(
    "https://discord.com/api/webhooks/1210626772010270780/y7ILzVd9h9bU3SHQKUQ_x5g20--WIO9dT_CtWrS2Q-OMTxZFNH7fwjZT1eQ_EVRT9jLm",
    message=message,
)
