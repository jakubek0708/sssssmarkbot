import discord
from discord.ext import *
from discord.ext import commands
import os
from dotenv import load_dotenv
import datetime
import asyncio

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ',', intents=intents)

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
# ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
# ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
# ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
# ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
# ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
# ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
# ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
# ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
# ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
# ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀
# siema nigger

@client.event
async def on_ready():
    print("czesc smark")

#loading .env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LOG_CHANNEL = os.getenv('LOG_CHANNEL')
BOT_SNOWFLAKE = os.getenv('BOT_SNOWFLAKE')

#variables:
log_channel = int(LOG_CHANNEL)
bot_snowflake = int(BOT_SNOWFLAKE)
slownik = {}
who_joined = None

@client.event
async def on_member_join(member):
    global embed_send, who_joined

    who_joined = member

    channel = client.get_channel(log_channel)

    pfp = member.avatar_url_as(size=32)

    embed=discord.Embed(description = f'{member.mention} {member}', color=0xf28500)
    embed.set_author(icon_url=pfp, name = 'Member Joined')
    embed.set_footer(text=f'{member.id}', icon_url=pfp)
    embed.add_field(name='User verification pending', value=f'Account created at: `{str(member.created_at)[:-7]}`', inline=False)
    embed.timestamp = datetime.datetime.utcnow()

    embed_send = await channel.send(embed=embed)


    slownik[embed_send.id] = member

    await embed_send.add_reaction('✅')
    await embed_send.add_reaction('❌')




@client.event
async def on_reaction_add(reaction, user):
    channel = client.get_channel(log_channel)
    pfp = who_joined.avatar_url_as(size=32)

    if str(reaction.emoji) == '✅' and user.id != bot_snowflake:

        var = discord.utils.get(user.guild.roles, name = "kumpel")
        await slownik[reaction.message.id].add_roles(var)

        await reaction.message.remove_reaction('✅', user)

        await reaction.message.remove_reaction('✅', user.guild.get_member(bot_snowflake))
        await reaction.message.remove_reaction('❌', user.guild.get_member(bot_snowflake))

        embed_verified=discord.Embed(description = f'{who_joined.mention} {who_joined}', color=0x66ff33)
        embed_verified.set_author(icon_url=pfp, name = 'Member Joined')
        embed_verified.set_footer(text=f'{user.id}', icon_url=pfp)
        embed_verified.add_field(name=f'Verified by: {user}', value=f'Account created at: `{str(who_joined.created_at)[:-7]}`', inline=False)
        embed_verified.timestamp = datetime.datetime.utcnow()

        await embed_send.edit(embed=embed_verified)


    if str(reaction.emoji) == '❌' and user.id != bot_snowflake:

        await user.guild.kick(slownik[reaction.message.id])

        await reaction.message.remove_reaction('❌', user)

        await reaction.message.remove_reaction('✅', user.guild.get_member(bot_snowflake))
        await reaction.message.remove_reaction('❌', user.guild.get_member(bot_snowflake))

        embed_kicked=discord.Embed(description = f'{who_joined.mention} {who_joined}', color=0xff0000)
        embed_kicked.set_author(icon_url=pfp, name = 'Member Joined')
        embed_kicked.set_footer(text=f'{who_joined.id}', icon_url=pfp)
        embed_kicked.add_field(name=f'Kicked by: {user}', value=f'Account created at: `{str(who_joined.created_at)[:-7]}`', inline=False)
        embed_kicked.timestamp = datetime.datetime.utcnow()

        await embed_send.edit(embed=embed_kicked)


@client.event
async def on_member_remove(member):
    channel = client.get_channel(log_channel)
    pfp = who_joined.avatar_url_as(size=32)
    channel = client.get_channel(log_channel)

    embed_left=discord.Embed(description = f'{who_joined.mention} {who_joined}', color=0xff0000)
    embed_left.set_author(icon_url=pfp, name = 'Member Left')
    embed_left.set_footer(text=f'{who_joined.id}', icon_url=pfp)
    embed_left.add_field(name=f'Account created at: ', value=f'`{str(who_joined.created_at)[:-7]}`', inline=False)
    embed_left.timestamp = datetime.datetime.utcnow()

    await channel.send(embed=embed_left)

@client.command()
async def test(ctx):
    await ctx.send("kappa 123")

client.run(TOKEN)
