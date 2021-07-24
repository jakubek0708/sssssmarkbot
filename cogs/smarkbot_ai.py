from discord.ext import tasks, commands
import discord 

import asyncio 

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('smarkbot ai')
trainer = ListTrainer(chatbot)


append_string = ""

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
            self.ai_training_list.append(message.content)


    @tasks.loop(minutes=2.5)
    async def learner(self):
        print("trying to learn")
        trainer.train(self.ai_training_list)
        print("learned something new :)))) hail hitler allah issalah slava ukrainie swine")
        self.ai_training_list.clear()
        print("deleted list information")

    @commands.command()
    async def show_list(self, ctx):
        await ctx.send(self.ai_training_list)
        

def setup(client):
    client.add_cog(smarkbot_ai(client))