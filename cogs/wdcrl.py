from discord.ext import commands
import discord 

class creditscore(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def creditscore(self, ctx, *, content):
        data = list(content.split(" "))
        if len(data) == 2:
            await ctx.send('错误')
        else: 
            print(content)
            print(data, data[0], data[1])
        

def setup(client):
    client.add_cog(creditscore(client))
