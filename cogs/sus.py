import discord
from discord.ext import commands
import datetime
import random

sussy_messages = []

smarkbot_zjeb = [
                'zabrałeś mi cel w życiu głupia kurwo',
                'utkaj łeb jebany bocie',
                'powiedz mi kto ci kurwa dał permy do odzywania się',
                'zneix, wyłącz tego zjeba błagam',
                '<:trollcrazy:800421758099783710> zamknij ryj'
]

class sus(commands.Cog):  # that class is sussy

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        global zmywara_time

        smarkownia = self.client.get_guild(id=489137343148851210)

        zmywara = discord.utils.get(smarkownia.roles, name='RANGA DZIEWCZYNA')
        if 'sus' in message.content.lower():
            await message.add_reaction('<:trollcrazy:800421758099783710>')
            sussy_messages.append(message.id)

        if message.content.lower() == 'e':
            await message.add_reaction('<a:peepoHappyJAM:832655294500831295>')

        if str(message.author.id) == 563303463748894721:
            ctx = await self.client.get_context(message)
            await ctx.send(random.choice(smarkbot_zjeb))


def setup(client):
    client.add_cog(sus(client))
