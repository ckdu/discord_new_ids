import discord

token = "" # bot token
channelId = 0 # channel id to send new member ids in

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        await client.get_channel(channelId).send(member.id)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(token)
