from discord.ext import commands
import discord
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



class dbreload(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dbreload(self, ctx):
        try:
            mycol = mydb[str(ctx.guild.id)]
            print(mycol.drop())
            mycol.insert_one({'_id': ctx.guild.id,
                            'name': ctx.guild.name,
                            'membersJoinLeaveLogs': False,
                            'logsChannellID': None,
                            'roleJoinID': None,
                            'roles': []})

            await ctx.send('Database reloaded')
        except:
            await ctx.send('Error okórd')



def setup(client):
    client.add_cog(dbreload(client))
