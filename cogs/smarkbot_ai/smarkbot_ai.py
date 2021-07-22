from discord.ext import commands
import discord 

class smarkbot_ai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("ai passed test suck fuck xd")

def setup(client):
    client.add_cog(smarkbot_ai(client))
