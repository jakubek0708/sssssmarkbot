from discord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

def setup(client):
    client.add_cog(test(client))
