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
    "url here",
    message=message,
)
