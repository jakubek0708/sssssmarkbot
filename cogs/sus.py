import discord
from discord.ext import commands
import datetime

sussy_messages = []

zmywara_time = None

class sus(commands.Cog): #that class is sussy

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        global zmywara_time

        smarkownia = self.client.get_guild(id=489137343148851210)

        zmywara = discord.utils.get(smarkownia.roles, name = 'RANGA DZIEWCZYNA')
        if 'sus' in message.content.lower():
            await message.add_reaction('<:trollcrazy:800421758099783710>')
            sussy_messages.append(message.id)

        if message.content.lower() == 'e':
            await message.add_reaction('<a:peepoHappyJAM:832655294500831295>')

        if zmywara in message.author.roles:

            now = datetime.datetime.now()
            if zmywara_time is not None:
                if now > zmywara_time + datetime.timedelta(hours=1):
                    ctx = await self.client.get_context(message)
                    await ctx.send('utkaj łeb zmywara')
                    zmywara_time = datetime.datetime.now()
            else:
                zmywara_time = datetime.datetime.now()

def setup(client):
    client.add_cog(sus(client))
