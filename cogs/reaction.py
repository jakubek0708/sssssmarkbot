import discord
from discord.ext import commands
import datetime
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_PORT = int(MONGO_PORT)
myclient = pymongo.MongoClient(
    f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']

what_reaction_clicked = {}
bot_snowflake = 822169790801641474

troll_messages = []


class leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        mycol = mydb[str(user.guild.id)]

        document = mycol.find_one({'_id': user.guild.id})

        if str(reaction.emoji) == '✅' and user.id != bot_snowflake:

            from .join import send_verification_messages_ids, member_joined_dict, embed_send, slownik, who_joined

            if reaction.message.id in send_verification_messages_ids:

                who_joined = member_joined_dict[reaction.message.id]

                pfp = who_joined.avatar_url_as(size=32)

                var = discord.utils.get(user.guild.roles, name=document['roleJoinID'])
                await slownik[reaction.message.id].add_roles(var)

                await reaction.message.remove_reaction('✅', user)

                await reaction.message.remove_reaction('✅', user.guild.get_member(bot_snowflake))
                await reaction.message.remove_reaction('❌', user.guild.get_member(bot_snowflake))

                embed_verified = discord.Embed(
                    description=f'{who_joined.mention} {who_joined}', color=0x66ff33)
                embed_verified.set_author(icon_url=pfp, name='Member Joined')
                embed_verified.set_footer(text=f'{user.id}', icon_url=pfp)
                embed_verified.add_field(
                    name=f'Verified by: {user}', value=f'Account created at: `{str(who_joined.created_at)[:-7]}`', inline=False)
                embed_verified.timestamp = datetime.datetime.utcnow()

                await send_verification_messages_ids[reaction.message.id].edit(embed=embed_verified)

        if str(reaction.emoji) == '❌' and user.id != bot_snowflake:

            from .join import send_verification_messages_ids, member_joined_dict, embed_send, slownik, who_joined

            if reaction.message.id in send_verification_messages_ids:

                who_joined = member_joined_dict[reaction.message.id]

                pfp = who_joined.avatar_url_as(size=32)

                await user.guild.kick(slownik[reaction.message.id])

                await reaction.message.remove_reaction('❌', user)

                await reaction.message.remove_reaction('✅', user.guild.get_member(bot_snowflake))
                await reaction.message.remove_reaction('❌', user.guild.get_member(bot_snowflake))

                embed_kicked = discord.Embed(
                    description=f'{who_joined.mention} {who_joined}', color=0xff0000)
                embed_kicked.set_author(icon_url=pfp, name='Member Joined')
                embed_kicked.set_footer(text=f'{who_joined.id}', icon_url=pfp)
                embed_kicked.add_field(
                    name=f'Kicked by: {user}', value=f'Account created at: `{str(who_joined.created_at)[:-7]}`', inline=False)
                embed_kicked.timestamp = datetime.datetime.utcnow()

                await send_verification_messages_ids[reaction.message.id].edit(embed=embed_kicked)

        if str(reaction.emoji) == '<:sus:820070011070185503>' and user.id != bot_snowflake:
            await reaction.message.add_reaction('<:trollcrazy:800421758099783710>')
            troll_messages.append(reaction.message.id)


def setup(client):
    client.add_cog(leave(client))
