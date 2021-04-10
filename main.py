import discord
from discord.ext import *
from discord.ext import commands
import os
from mcstatus import MinecraftServer
from dotenv import load_dotenv
import datetime
import asyncio

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = ',', intents=intents)

#loading .env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LOG_CHANNEL = os.getenv('LOG_CHANNEL')
BOT_SNOWFLAKE = os.getenv('BOT_SNOWFLAKE')
PORT = int(os.getenv('PORT'))
SERVER_IP = os.getenv('SERVER_IP')

#minecraft server search
server = MinecraftServer(SERVER_IP, PORT)



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
# sussus amogus

#
# ░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
# ░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
# ░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
# ░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
# ░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
# █░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
# █░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
# ░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
# ░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
# ░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
# ░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
# ░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
# ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
# ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
# ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
# YOU'VE BEEN TROLLED

@client.event
async def on_ready():
    print("czesc smark")

#variables:
log_channel = int(LOG_CHANNEL)
bot_snowflake = int(BOT_SNOWFLAKE)
slownik = {}
who_joined = None
test_channel = 768015589444419588
send_verification_messages_ids = []

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

    send_verification_messages_ids.append(embed_send.id)
    slownik[embed_send.id] = member

    await embed_send.add_reaction('✅')
    await embed_send.add_reaction('❌')


emoji_list = ['<:SS:827162978662875188>', '<:S_:827163027157286923>', '<:A_:827163066289487902>', '<:B_:827163087370715166>', '<:C_:827163109415452713>', '<:D_:827163128155602944>']

what_reaction_clicked = {}
@client.event
async def on_reaction_add(reaction, user):


    if str(reaction.emoji) == '✅' and user.id != bot_snowflake and reaction.message.id in send_verification_messages_ids:
        channel = client.get_channel(log_channel)
        pfp = who_joined.avatar_url_as(size=32)

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


    if str(reaction.emoji) == '❌' and user.id != bot_snowflake and reaction.message.id in send_verification_messages_ids:
        channel = client.get_channel(log_channel)
        pfp = who_joined.avatar_url_as(size=32)

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

#    if str(reaction.emoji) in emoji_list and user.id != bot_snowflake and reaction.message.id in clicked:
#        channel = client.get_channel(test_channel)
#        if user not in clicked[reaction.message.id]:
#
#            print('clicked grape')
#            clicked[reaction.message.id].append(user)
#            what_reaction_clicked[user] = reaction
#        else:
#            print('clicked before')
#            await reaction.message.remove_reaction(reaction, user)
#
#    if self_vote_protection[reaction.message.id] == user.id and user.id != bot_snowflake and reaction.message.id in clicked:
#
#        await reaction.message.remove_reaction(reaction, user)
#
#@client.event
#async def on_reaction_remove(reaction, user):
#    print(user)
#    if str(reaction.emoji) in emoji_list and user.id != bot_snowflake and reaction.message.id in clicked and reaction == what_reaction_clicked[user]:
#        clicked[reaction.message.id].remove(user)


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
async def players(ctx):

    try:
        query = server.query()
        players = ", ".join(query.players.names)
        if players:
            await ctx.send(f'Na serwerze jest: {players}')
        else:
            await ctx.send('Nikogo nie ma')

    except:
        await ctx.send('Nie mogę się połączyć z serwerem xd')



@client.command()
async def fanfik(ctx):
    await ctx.send("chłopacy jaki fanfik o co chodzi")

@client.command()
async def echo(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

clicked = {}
self_vote_protection = {}

#@client.command()
#async def vote(ctx):
#    global clicked
#    name_list = {'Smark': 293079974787678209,
#    'Spki': 414932696285052938,
#    'Desu': 350331531472011285,
#    'Mesimov': 293400827295563778,
#    'Celled': 172108539144306698,
#    'Pondoryna': 804418160186753025,
#    'Heryin': 265085929809510402,
#    'Witt': 226646760515305473,
#    'Toxic': 390956680705474571,
#    'Tadziu': 282421992051703809,
#    'Catto': 172108539144306698,
#    'Aamon': 269843173218582548,
#    'Awawa': 307541751248453632,
#    'Zoomek': 292634117084807168,
#    'Iza': 681541408074629120,
#    'Rayz': 564133511632781353,
#    'Ravioli': 437320877114261515,
#    'Ojciec': 263784520900280332,
#    'Moneyigos': 294936820595163142,
#    'Czesio': 535464141620510721,
#    'Igoruwa': 390926589640179712,
#    'Jager': 730209739736350770,
#    'Haav': 386209774481571841,
#    'Zneix': 288028423031357441,
#    'Stalowy': 327402104446648331,
#    'Wiktor': 475969701969788938}
#
#    for message in name_list:
#        vote_message = await ctx.send(message)
#
#        self_vote_protection[vote_message.id] = name_list[message]
#
#        for i in emoji_list:
#            await vote_message.add_reaction(i)
#
#        clicked[vote_message.id] = []

client.load_extension("cogs.test")

client.run(TOKEN)
