from discord.ext import commands

class threadrm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_thread_join(thread):
        try:
            await thread.delete()
        except:
            print('failed to remove thread')


def setup(client):
    client.add_cog(threadrm(client))
