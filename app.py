import os
import time
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load variables from .env into the system env.
load_dotenv()
# Initializes your app with your bot token and socket mode handler
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

# Listens for the ping command and responds with the latency
@app.command("/sarvagyan-ping")
def ping_cmd_response(ack, body, respond):

    start = time.time_ns() 
    ack()
    latency = (time.time_ns() - start) / 1000000
    
    respond(f"Sarvagyan up and running. Latency: {latency} ms")



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

