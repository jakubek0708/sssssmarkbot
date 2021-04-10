from discord.ext import commands

class echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

def echo(client):
    client.add_cog(test(client))
