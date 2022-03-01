import os

import requests

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def to_discord(message: str, webhook: str = DISCORD_WEBHOOK_URL) -> None:
    if not webhook:
        return

    data = {"content": message}

    requests.post(webhook, data=data)
