import discord
from discord.ext import commands

sussy_messages = []

smarkownia = self.client.get_guild(id=489137343148851210)

zmywara = discord.utils.get(smarkownia.roles, name = 'RANGA DZIEWCZYNA')

class sus(commands.Cog): #that class is sussy

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'sus' in message.content.lower():
            await message.add_reaction('<:trollcrazy:800421758099783710>')
            sussy_messages.append(message.id)

        if message.content.lower() == 'e':
            await message.add_reaction('<a:peepoHappyJAM:832655294500831295>')

        if zmywara in message.author.roles:
            ctx = await client.get_context(message)
            await ctx.send('utkaj łeb zmywara')

def setup(client):
    client.add_cog(sus(client))
