import os

import requests
from dotenv import load_dotenv

load_dotenv()
TwitterBearerToken = os.environ["TWITTER_BEARER_TOKEN"]

add_data = {"add": [{"value": ""}]}

delete_data = {"delete": {"ids": []}}

header = {"Authorization": f"Bearer {TwitterBearerToken}"}
res = requests.post(
    "https://api.twitter.com/2/tweets/search/stream/rules",
    headers=header,
    json=add_data,
)

print(res.text)
