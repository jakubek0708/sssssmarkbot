from discord.ext import commands

class smark(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def smark(self, ctx):
        server = self.client.get_guild(id=489137343148851210)
        smark = server.get_member(293079974787678209)
        await ctx.send(ctx.message.author.nick)
        await ctx.send(smark.status)

def setup(client):
    client.add_cog(smark(client))
