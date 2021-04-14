import discord
from discord.ext import commands
import pymongo
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
MONGO_PORT = int(os.getenv('MONGO_PORT'))

myclient = pymongo.MongoClient(f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):

        mycol = mydb[str(ctx.message.guild.id)]

        document = mycol.find_one({'_id': ctx.message.guild.id})

        if document['membersJoinLeaveLogs']:
            logs_status = 'on'
        else:
            logs_status = 'off'


        embed=discord.Embed(title="Info", description="statuses:", color=0x00e1ff)
        embed.add_field(name="Logs:", value=logs_status, inline=False)
        embed.add_field(name="Log channel ID:", value=document['logsChannellID'], inline=False)
        embed.add_field(name="Acceptance role:", value=document['roleJoinID'], inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(info(client))
