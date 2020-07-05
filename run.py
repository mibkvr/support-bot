from TicketBot import TicketBot




import os
import threading

token = os.environ.get("DISCORD_TOKEN")

if token is None or len(token) < 5:
    raise Exception("Discord Token is not valid")

client = TicketBot()


client.run(token)
