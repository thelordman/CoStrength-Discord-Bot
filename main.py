import discord
import os

client = discord.Client()
token = os.environ['TOKEN']

@client.event
async def on_ready():
  print("JDA Ready")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith("!ass"):
    await msg.channel.send("http://cdn.megabuttpics.com/images/biggest-ssbbw-large-bottom.jpg")

client.run(token)