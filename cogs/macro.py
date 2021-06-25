from discord.ext import tasks, commands
from discord.ext.commands import has_permissions
import asyncio


class macro(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def macro(self, ctx, *, message):

        lista = message.split(" ")

        if len(lista) == 2:
            try:
                float(lista[1]) #delay
                int(lista[2])
            except:
                await ctx.send('eeeeee daj numer na koncu sekundy maja byc co ile sekund spam czaisz albo kurwa tam na tyle ma tez byc kurwa ten czaisz ile ma byc spamu kumasz???')
            
            what_spam = lista[0]
            delay = float(lista[1])
            how_many = int(lista[2])

            for i in range(how_many):
                asyncio.sleep(delay)
                await ctx.send(what_spam)





    

def setup(client):
    client.add_cog(macro(client))
