from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle


CLIENTS = []

for SESSION in SESSIONS:
    if SESSION:
        client = Client(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="ᕼᗩᖇꇙᕼᑌXD"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("Wrostdemon")
            CLIENT.join_chat("HarshuXDBots")
            print(f"---> Client {i+1} has been Started...")
        except Exception as e:
            print(e)

    print("💞YOUR ᕼᗩᖇꇙᕼᑌˣᴰ SPAM USERBOTS DEPLOYED SUCCESSFULLY 💞")
    idle()
