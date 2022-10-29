from webserver import keep_alive
import requests

channelID = 756173881697370233
headers = {
    "authorization":
    "MTAzNDg4NTExODQwNzQ5NTcwMA.GVtIZK.xp9xXawsumFU-x7gzLPYxWopmC7PLQvg3Ch0SQ"
}
keep_alive()
file = open("GodXiii", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
