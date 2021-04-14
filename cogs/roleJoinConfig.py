import discord
from discord.ext import commands
from dotenv import load_dotenv
import pymongo
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
MONGO_PORT = int(os.getenv('MONGO_PORT'))

myclient = pymongo.MongoClient(f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']

class roleConfig(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roleConfig(self, ctx, *, message):
        mycol = mydb[str(ctx.message.guild.id)] #collection
        content = message
        document = mycol.find_one({'_id': ctx.message.guild.id})
        print(type(content))
        try:
            discord.utils.get(ctx.message.guild.roles, name = content)
            mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'roleJoinID': content}})
            await ctx.send(f'Zmieniłem rolę na `{content}`')
        except:
            await ctx.send('Nie mogę znaleźć roli, upewnij się, że dałeś jej nazwę (nie pinguj jej, po prostu nazwa)')



def setup(client):
    client.add_cog(roleConfig(client))
