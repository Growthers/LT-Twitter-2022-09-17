import threading

from dotenv import load_dotenv

from twitter import stream
from websocket_connection import ws

load_dotenv()


if __name__ == "__main__":
    stream_thread = threading.Thread(target=stream)
    stream_thread.start()
    ws.run_forever()
