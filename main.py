import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()
token = os.environ['TOKEN']

sad_words = ["sad", "depress", "unhappy", "angry", "miserabl", "mad", "kill you", "bad"]
sad_responses = ["L", "ur so bad", "lmao", "lol", "kys", "damn u suck", "Loser!", "everyone hates you!"]

@client.event
async def on_ready():
  print("Client Ready")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith("!ass"):
    await msg.reply("http://cdn.megabuttpics.com/images/biggest-ssbbw-large-bottom.jpg")

  if any(word in msg.content.lower() for word in sad_words):
    await msg.channel.send(random.choice(sad_responses))

  if msg.content.startswith("costrength"):
    await msg.channel.send("yo")

  if msg.content.startswith("no u"): 
    await msg.channel.send("no u")

keep_alive()
client.run(token)