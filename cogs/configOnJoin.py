import discord
from discord.ext import commands
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


class ServerJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        mycol = mydb[str(guild.id)]
        print(mycol.drop())
        print(f'joined {guild.name}')
        mycol.insert_one({'_id': guild.id,
                          'name': guild.name,
                          'membersJoinLeaveLogs': False,
                          'logsChannellID': None,
                          'roleJoinID': None,
                          'roles': []})


def setup(client):
    client.add_cog(ServerJoin(client))
