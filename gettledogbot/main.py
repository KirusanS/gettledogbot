import discord
import asyncio
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('g1'):
        for user in message.mentions:
            msg = '<:gettledawg:499326197159952395> {}'.format(user.mention)
            await client.send_message(message.channel, msg)
    elif message.content.startswith('g2'):
        for user in message.mentions:
            msg = '<:gettledawg2:501546788277190666> {}'.format(user.mention)
            await client.send_message(message.channel, msg)
    elif message.content.startswith('who is a good'):
      for user in message.mentions:
        msg = '<:gettledawg2:501546788277190666> {}'.format(user.mention)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('g3'):
        for user in message.mentions:
            msg = '<:gettledog3:507659745767981057> {}'.format(user.mention)
            await client.send_message(message.channel, msg)
    elif message.content == "gd1e":
        await client.send_message(message.channel, "<:gettledawg:499326197159952395> @everyone")  
    elif message.content == "gd2e":
        await client.send_message(message.channel, "<:gettledawg2:501546788277190666>  @everyone")      
    elif message.content == "gd3e":
     await client.send_message(message.channel, "<:gettledog3:507659745767981057>  @everyone")
    elif message.content == "gettledoghelp":
      await client.send_message(message.channel, "**Gettledog Help** \n **g1** - ping your friends with gettledog1 \n **g2** - ping your friends with gettledog2 \n **g3** - ping your friends with gettledog3 \n **gd1e** - ping everyone with gettledog1 \n **gd2e** - ping everyone with gettledog2 \n **gd3e** - ping everyone with gettledog3 \n")

    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

keep_alive()
client.run('NTQ3MTMyMTE4NjEwNzM5MjI2.D0yU-Q.9HlndBU5YgJQuL0ccAbX0_FkTfc')