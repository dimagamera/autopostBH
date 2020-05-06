from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync
from settings import api_id, api_hash
#
client = TelegramClient("test", api_id, api_hash)
client.start()
print("STARTED")

@client.on(events.NewMessage(chats=["https://t.me/haccking", "https://t.me/overlamer1", "https://t.me/joinchat/AAAAAEbZ5-nUFjyx3cjbug", "https://t.me/under_public"]))
async def normal_handler(event):
    if isinstance(event.chat, types.Channel):
        username = event.chat.username
    await client.send_message("https://t.me/joinchat/AAAAAE_-kL_c1M7B4a5IYg", event.message)

client.run_until_disconnected()
