import os
import time
import random
from tavily import TavilyClient
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load variables from .env into the system env.
load_dotenv()
# Initializes your app with your bot token and socket mode handler
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

# Listens for the ping command and responds with the latency
@app.command("/sarvgyan-ping")
def ping_cmd_response(ack, body, respond):

    start = time.time_ns() 
    ack()
    latency = (time.time_ns() - start) / 1000000

    respond(f"Sarvgyan up and running. Latency: {latency} ms")

@app.command("/sarvgyan-befunny")
def befunny_cmd_response(ack, body, respond):

    ack()

    jokes = [
    "The mathematician got lost because he took the wrong exponent.",
    "The skeleton went to the party, but had no body to go with.",
    "The programmer’s wife asked him to get milk. He never returned because the store had a “404: Milk Not Found.”",
    "The calendar got fired because its days were numbered.",
    "The scarecrow won an award because he was outstanding in his field."
    ]
    i = random.randint(0, 5)

    respond(f"Here I go: {jokes[i]} 🤣🤣🤣")

@app.command("/sarvgyan-search")
def search_cmd_response(ack, body, respond):

    ack()

    # Extract search query from the slack command
    search_query = body["text"]

    # Search for the requested query using Tavily API
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = tavily_client.search(search_query, include_answer=True)

    # Respond with AI answer for the search query
    respond(response["answer"])
    





# Start your app
if __name__ == "__main__":

    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()

