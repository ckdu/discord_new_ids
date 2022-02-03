# Settings
botToken = 'token here' # bot token
maxAccAge = 3 # Max account age in days to tolerate
maxJoinIntervalSeconds = 5 # Max join interval between accounts of maxAccAge
channelId = 0 # Channel ID to post the id's of detected bots

import discord
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('Logged in as', client.user)

lastNew = [None] * 2

@client.event
async def on_member_join(member):
    # Someone joined.
    if (datetime.utcnow() - member.created_at).days <= maxAccAge:
        # They are a new account.
        if lastNew[0] and lastNew[1]:
            # There was a previous new account who is the first in a potential many joining.
            if (datetime.utcnow() - lastNew[0]).seconds <= maxJoinIntervalSeconds:
                # The last 2 new accounts joined within the specified interval, reporting two potential bots.
                await client.get_channel(channelId).send(lastNew[1])
                await client.get_channel(channelId).send(member.id)
                lastNew[0] = datetime.utcnow()
                lastNew[1] = None

        elif lastNew[0] and not lastNew[1]:
            # There were 2 or more new accounts joining consecutively.
            if (datetime.utcnow() - lastNew[0]).seconds <= maxJoinIntervalSeconds:
                # This is another new account who joined within the specified interval, reporting as potential bot.
                await client.get_channel(channelId).send(member.id)
                lastNew[0] = datetime.utcnow()
            else:
                # Since they joined outside the interval, they may not be a bot. Resetting them to first new account.
                lastNew[0] = datetime.utcnow()
                lastNew[1] = member.id

        elif not lastNew[0]:
            # They are the first new account after starting the bot.
            lastNew[0] = datetime.utcnow()
            lastNew[1] = member.id

client.run(botToken)
