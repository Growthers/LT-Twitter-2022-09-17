from src.sending import to_discord


def process(tweet_data: dict) -> None:
    data = tweet_data["data"]
    includes = tweet_data["includes"]
    user = includes["users"][0]

    tweet_url = f"https://twitter.com/{user['username']}/status/{data['id']}"
    to_discord(tweet_url)
