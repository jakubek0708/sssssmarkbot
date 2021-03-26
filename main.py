import discord
from discord.ext import *
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!', intents=intents)



@client.event
async def on_ready():
    print("czesc smark")

#loading .env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LOG_CHANNEL = os.getenv('LOG_CHANNEL')
BOT_SNOWFLAKE = os.getenv('BOT_SNOWFLAKE')

#variables:
log_channel = LOG_CHANNEL
bot_snowflake = BOT_SNOWFLAKE
slownik = {}

@client.event
async def on_member_join(member):
    global verification_message
    channel = client.get_channel(log_channel)
    verification_message = await channel.send(f'śmieć -> {member}')
    slownik[verification_message.id] = member
    await verification_message.add_reaction('✅')
    await verification_message.add_reaction('❌')

@client.event
async def on_reaction_add(reaction, user):
  channel = client.get_channel(log_channel)

  if str(reaction.emoji) == '✅' and user.id != bot_snowflake:
    var = discord.utils.get(user.guild.roles, name = "kumpel")
    await slownik[reaction.message.id].add_roles(var)
    print(type(user))
    await reaction.message.remove_reaction('✅', user)
    await reaction.message.remove_reaction('✅', user.guild.get_member(bot_snowflake))
    await reaction.message.remove_reaction('❌', user.guild.get_member(bot_snowflake))


  if str(reaction.emoji) == '❌' and user.id != bot_snowflake:
    await user.guild.kick(slownik[reaction.message.id])
    await reaction.message.remove_reaction('❌', user)
    await reaction.message.remove_reaction('✅', user.guild.get_member(bot_snowflake))
    await reaction.message.remove_reaction('❌', user.guild.get_member(bot_snowflake))

@client.event
async def on_member_remove(member):
    channel = client.get_channel(log_channel)
    await channel.send(f'{member} spierdolił z serwera')
    user = member.server.get_member(member.id) # Fake snowflake, will not work
    if not user:
        return # Can't find the user, then quit
    pfp = user.avatar_url
    embed=discord.Embed(title="test", description='{}, test'.format(user.mention) , color=0xecce8b)
    embed.set_image(url=(pfp))
    await channel.send_message(message.channel, embed=embed)

#co kurwa

client.run(TOKEN)
