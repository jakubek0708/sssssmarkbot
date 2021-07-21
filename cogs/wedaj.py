from discord.ext import commands


class es(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dmsend(self, ctx, *, message):
        server = self.client.get_guild(id=489137343148851210)
        smark = server.get_member(386209774481571841)
        await smark.send(message)

        

def setup(client):
    client.add_cog(es(client))
