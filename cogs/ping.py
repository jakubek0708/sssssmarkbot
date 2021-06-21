from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'huj <a:forsenPls:612032287206408243> = {self.client.latency}ms')    
        
def setup(client):
    client.add_cog(ping(client))
