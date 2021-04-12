import discord
from discord.ext import commands

class sus(commands.Cog): #that class is sussy

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(message):
        if 'sus' in message.content:
            await message.add_reaction('<:trollcrazy:800421758099783710>')

def setup(client):
    client.add_cog(sus(client))
