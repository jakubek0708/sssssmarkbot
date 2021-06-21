from discord.ext import commands

class ping(commands.Cog):
    dev __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('huj <a:forsenPls:612032287206408243> ! {0}'.format(round(self.client.latency, 1)))    
        
dev setup(client):
    client.add_cog(ping(client))
