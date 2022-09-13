# LT-Twitter for 2022/09/17

poetryを導入してください

```
poetry install
pre-commit install
poetry run python src/main.py
```

`.env`
```
TWITTER_BEARER_TOKEN=
WEBSOCKET_URI=
```

### ルールを追加する

`src/add_rules.py`を編集してください
```
poetry run python src/add_rules.py
```

### ルールを取得する
```
poetry run python src/get_rules.py
```
