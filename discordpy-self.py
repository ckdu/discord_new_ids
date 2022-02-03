import time
import discord

token = "token" # Discord token
channelToWatch = 0 # Welcome channel ID
channelToSend = 0 # Channel ID to send the user ids
ids = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global ids

        if message.channel.id == channelToWatch:
            ids += str(message.author.id) + "\n"
        if ids.count("\n") > 4:
            sendIds = ids
            ids = ""
            await client.get_channel(channelToSend).send(sendIds)

client = MyClient()
client.run(token)
