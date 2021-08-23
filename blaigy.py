import discord
from discord.ext import commands
import embed



TOKEN = "ODc3NDc2MzUyNzg4Mzk4MTUw.YRzLiQ.BmdESQz2gOUv2Nn6g9m8OWKzFOg"
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("Ready when you are")


@client.event
async def on_message(message):
  if message.author.bot:
    return
  if message.content.startswith('https://discord.gg'):
      await message.delete()
      await message.author.send("בבקשה אל תשלח sever invites")


@client.event
async def on_message(message):
    
    
    msg_content = message.content.lower()

    curseWord = ['זונה', 'שרמוטה','הומו','חולה סרטן','סרטן','מזדיין','מזיין בתחת','בתחת','קוקסינל','יא קוקסינל','זין','בולבול','אוכל בתחת','']
    
    # delete curse word if match with the list
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.author.send("בבקשה אל תקלל")





client.run(TOKEN)