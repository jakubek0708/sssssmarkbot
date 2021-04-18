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
myclient = pymongo.MongoClient(f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']

class leave(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_remove(self, member):

        mycol = mydb[str(member.guild.id)] #collection

        document = mycol.find_one({'_id': member.guild.id})

        log_channel = int(document['logsChannellID'])

        who_joined = member

        channel = self.client.get_channel(log_channel)

        pfp = who_joined.avatar_url_as(size=32)


        embed_left=discord.Embed(description = f'{who_joined.mention} {who_joined}', color=0xff0000)
        embed_left.set_author(icon_url=pfp, name = 'Member Left')
        embed_left.set_footer(text=f'{who_joined.id}', icon_url=pfp)
        embed_left.add_field(name=f'Account created at: ', value=f'`{str(who_joined.created_at)[:-7]}`', inline=False)
        embed_left.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed_left)

def setup(client):
    client.add_cog(leave(client))
