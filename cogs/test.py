from discord.ext import commands

class test:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test failed damb")

def setup(client):
    client.add_cog(test(bot))
