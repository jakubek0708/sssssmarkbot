import discord
from discord.ext import commands

class smark(commands.Cog): #that class is sussy

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if after.status is discord.Status.online:
            print('smark żyje')

        elif after.status is discord.Status.online:
            print('smark nie żyje')
            
def setup(client):
    client.add_cog(smark(client))
