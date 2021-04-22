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

slownik = {}
who_joined = None
send_verification_messages_ids = {}
member_joined_dict = {}


class join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        mycol = mydb[str(member.guild.id)]

        document = mycol.find_one({'_id': member.guild.id})

        if document['membersJoinLeaveLogs']:
            global embed_send, who_joined

            log_channel = int(document['logsChannellID'])

            who_joined = member

            channel = self.client.get_channel(log_channel)

            pfp = member.avatar_url_as(size=32)

            embed = discord.Embed(description=f'{member.mention} {member}', color=0xf28500)
            embed.set_author(icon_url=pfp, name='Member Joined')
            embed.set_footer(text=f'{member.id}', icon_url=pfp)
            embed.add_field(name='User verification pending',
                            value=f'Account created at: `{str(member.created_at)[:-7]}`', inline=False)
            embed.timestamp = datetime.datetime.utcnow()

            embed_send = await channel.send(embed=embed)

            send_verification_messages_ids[embed_send.id] = embed_send

            member_joined_dict[embed_send.id] = who_joined

            slownik[embed_send.id] = member

            await embed_send.add_reaction('✅')
            await embed_send.add_reaction('❌')


def setup(client):
    client.add_cog(join(client))
