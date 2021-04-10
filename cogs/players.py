from discord.ext import commands
from dotenv import load_dotenv
from mcstatus import MinecraftServer
import os

load_dotenv()
PORT = int(os.getenv('PORT'))
SERVER_IP = os.getenv('SERVER_IP')

server = MinecraftServer(SERVER_IP, PORT)

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def players(self, ctx):

        try:
            query = server.query()
            players = ", ".join(query.players.names)
            if players:
                await ctx.send(f'Na serwerze jest: {players}')
            else:
                await ctx.send('Nikogo nie ma')

        except:
            await ctx.send('Nie mogę się połączyć z serwerem xd')




def setup(client):
    client.add_cog(test(client))
