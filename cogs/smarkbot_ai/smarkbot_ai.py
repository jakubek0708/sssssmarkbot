from discord.ext import commands
import discord 

class smarkbot_ai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 390956680705474571:
            await message.ctx.send(message)

def setup(client):
    client.add_cog(smarkbot_ai(client))
