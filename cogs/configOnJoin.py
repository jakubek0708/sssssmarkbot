import discord
from discord.ext import commands
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['smarkbot']

class ServerJoin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        mycol = mydb[guild.id]
        print(f'joined {guild.name}')
        server = {}
        mycol.insert_one({'_id':guild.id,
        'name': guild.name,
        'membersJoinLeaveLogs': False,
        'logsChannellID': None})


def setup(client):
    client.add_cog(ServerJoin(client))
