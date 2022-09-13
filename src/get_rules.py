import os

import requests
from dotenv import load_dotenv

load_dotenv()
TwitterBearerToken = os.environ["TWITTER_BEARER_TOKEN"]

header = {"Authorization": f"Bearer {TwitterBearerToken}"}
res = requests.get(
    "https://api.twitter.com/2/tweets/search/stream/rules", headers=header
)

print(res.text)
