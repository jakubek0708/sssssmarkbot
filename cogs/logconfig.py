import discord
from discord.ext import commands
from dotenv import load_dotenv
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_PORT = int(MONGO_PORT)
myclient = pymongo.MongoClient(f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']

class logconfig(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def logconfig(self, ctx, *, message):
        mycol = mydb[str(ctx.message.guild.id)] #collection
        content = message
        document = mycol.find_one({'_id': ctx.message.guild.id})

        try:
            content = int(content)
        except:
            pass

        if type(content) == int:
            mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'logsChannellID': content}})
            await ctx.send(f'Ustawiono log channel jako: {content}')

        elif type(content) == str:
            if document['logsChannellID'] != None:
                if content == 'on':
                    mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'membersJoinLeaveLogs': True}})
                    await ctx.send('Turned to: `on`')
                elif content == 'off':
                    mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'membersJoinLeaveLogs': False}})
                    await ctx.send('Turned to: `off`')
                else:
                    await ctx.send('Dostępne tylko: `on` i `off`')
            else:
                await ctx.send('Musisz na początku określić na jakim kanale mają się pojawiać logi -> `logconfig id kanału`')
        else:
            await ctx.send('Error, pajton exploded')


def setup(client):
    client.add_cog(logconfig(client))
