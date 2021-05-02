import discord
from discord.ext import commands
import datetime
import random

sussy_messages = []

smarkbot_time = None



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
        global smarkbot_time

        smarkownia = self.client.get_guild(id=489137343148851210)

        zmywara = discord.utils.get(smarkownia.roles, name='RANGA DZIEWCZYNA')
        if 'sus' in message.content.lower():
            await message.add_reaction('<:trollcrazy:800421758099783710>')
            sussy_messages.append(message.id)

        if message.content.lower() == 'e':
            await message.add_reaction('<a:peepoHappyJAM:832655294500831295>')

        if zmywara in message.author.roles:
            now = datetime.datetime.now()

            if smarkbot_time is not None:
                if now > smarkbot_time + datetime.timedelta(hours=6):
                    ctx = await self.client.get_context(message)
                    await ctx.send(random.choice(smarkbot_zjeb))
                    smarkbot_time = datetime.datetime.now()
            else:
                smarkbot_time = datetime.datetime.now()


def setup(client):
    client.add_cog(sus(client))
