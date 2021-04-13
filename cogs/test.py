from discord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test failed damb")
        await ctx.send(ctx.message.guild.id)
def setup(client):
    client.add_cog(test(client))
