from discord.ext import commands


class spij(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spij(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


def setup(client):
    client.add_cog(spij(client))
