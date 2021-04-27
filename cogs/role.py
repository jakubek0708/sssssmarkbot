import discord
from discord.ext import commands
from dotenv import load_dotenv
import pymongo
import os
from discord.ext.commands import has_permissions
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_PORT = int(MONGO_PORT)

myclient = pymongo.MongoClient(
    f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']


class role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def role(self, ctx, *, message):
        lista = ["aa", "xd"]
        lista_str = ", ".join(lista)
        await ctx.send(message)
        


def setup(client):
    client.add_cog(role(client))