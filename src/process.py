import json

# from sending import to_discord
from websocket_connection import ws


def process(tweet_data: dict) -> None:
    data = tweet_data["data"]
    includes = tweet_data["includes"]
    user = includes["users"][0]

    username = user["username"]

    # tweet_url = f"https://twitter.com/{username}/status/{data['id']}"
    # to_discord(tweet_url)

    isRT = False

    if "referenced_tweets" in data:
        if data["referenced_tweets"][0]["type"] == "retweeted":
            isRT = True

    if isRT:
        return

    text = data["text"]

    sending_data = {
        "type": "COMMENTS",
        "payload": {
            "platform": "twitter",
            "name": f"{user['name']}(@{username})",
            "iconUrl": user["profile_image_url"],
            "content": text,
        },
    }
    print(sending_data)
    ws.send(json.dumps(sending_data))
