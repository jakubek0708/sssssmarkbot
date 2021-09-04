from discord.ext import commands
import discord 

class creditscore(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def creditscore(self, ctx, *, content):
        data = list(content.split(" "))
        if len(data) == 2:
            try:
                await ctx.message.server.get_member(int(data[0][2:-1]))
            except: 
                await ctx.send('错误 kurwa')
        else: 
            await ctx.send('错误')
        

def setup(client):
    client.add_cog(creditscore(client))
