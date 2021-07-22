from discord.ext import commands
import discord 

append_string = ""
last_user_id = None

class smarkbot_ai(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ai_training_list = []

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.client.process_commands(message)
        global append_string
        global last_user_id

        if message.author.id in [390956680705474571, 293079974787678209]:
            while message.author.id == last_user_id: 
                append_string += message.content 
            else:
                self.ai_training_list.append(append_string)
            
            append_string = message.content
            last_user_id = message.author.id 

    @commands.command()
    async def show_list(self, ctx):
        await ctx.send(self.ai_training_list)
        

def setup(client):
    client.add_cog(smarkbot_ai(client))
