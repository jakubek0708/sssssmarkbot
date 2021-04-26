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
    async def role(self, ctx):
        lista = ["aa", "https://media.discordapp.net/attachments/764447332288561152/822936777811427369/image0_4.gif"]
        lista_str = ", ".join(lista)
        await ctx.send(lista_str)
        


def setup(client):
    client.add_cog(role(client))