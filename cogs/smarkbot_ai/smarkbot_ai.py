from discord.ext import commands
import discord 

class smarkbot_ai(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ai_training_list = []

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 390956680705474571:
            ctx = await self.client.get_context(message)
            await ctx.send(message.content)
            self.ai_training_list.append(message.content)
            
    @commands.command()
    async def show_list(self, ctx):
        await ctx.send(self.ai_training_list)
        

def setup(client):
    client.add_cog(smarkbot_ai(client))
