import json
import os

import requests


def notify(message: str, stdout=True):
    webhook = os.getenv("SLACK_WEBHOOK")
    try:
        requests.post(webhook, data=json.dumps({"text": message}))
    except:
        pass
    if stdout:
        print(message)
