from discord.ext import commands

class threadrm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_thread_create(thread):
        print(1)
        await thread.delete()
        print(2)

def setup(client):
    client.add_cog(threadrm(client))
