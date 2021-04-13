from discord.ext import commands
from dotenv import load_dotenv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['smarkbot']

class logconfig(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def logconfig(self, ctx):
        mycol = mydb[ctx.message.guild.id] #collection

        content = ctx.message.content

        document = mycol.find_one({'_id': ctx.message.guild.id})

        if type(content) == int:
            if document['membersJoinLeaveLogs']:
                mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'logsChannellID': content}})
                await ctx.send(f'Ustawiono log channel jako: {content}')
            else:
                await ctx.send('Musisz na początku włączyć logi -> `logconfig on`')

        elif type(content) == str:
            if content == 'on':
                mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'membersJoinLeaveLogs': True}})
                await ctx.send('Turned to: on')
            elif content == 'off':
                mycol.update_one({'_id': ctx.message.guild.id}, {'$set': {'membersJoinLeaveLogs': False}})
                await ctx.send('Turned to: off')

def setup(client):
    client.add_cog(logconfig(client))
