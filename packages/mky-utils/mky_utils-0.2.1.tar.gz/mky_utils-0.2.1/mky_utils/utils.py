import json
import os
import random

import requests


def notify(message: str, stdout=True):
    webhook = os.getenv("SLACK_WEBHOOK")
    try:
        requests.post(webhook, data=json.dumps({"text": message}))
    except:
        pass
    if stdout:
        print(message)


def generate_name() -> str:
    names = []

    for generation in range(1, 5):
        response = requests.get(f"https://pokeapi.co/api/v2/generation/{generation}/")
        generation_data = response.json()
        for name in generation_data["pokemon_species"]:
            names.append(name["name"])

    response = requests.get(
        "https://raw.githubusercontent.com/dariusk/corpora/master/data/words/adjs.json"
    )
    adjectives_data = response.json()
    adjectives_list = adjectives_data["adjs"]
    return f"{random.choice(adjectives_list)}-{random.choice(names)}"
