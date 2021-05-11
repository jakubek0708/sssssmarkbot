from discord.ext import commands


class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        server = self.client.get_guild(id=489137343148851210)
        smark = server.get_member(293079974787678209)
        await smark.send("Ej bo pracę domową mam z infy")
        await smark.send("Mógłbyś ten?")
        await smark.send("dać mi może? jak masz zrobioną")
        await smark.send("no bo mi maszyna nie działa")
        

def setup(client):
    client.add_cog(test(client))
