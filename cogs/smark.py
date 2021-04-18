from discord.ext import commands

class smark(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def smark(self, ctx):
        await ctx.send(client.get_user(293079974787678209).nick)


def setup(client):
    client.add_cog(smark(client))
