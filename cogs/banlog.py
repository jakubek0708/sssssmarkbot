import discord
from discord.ext import commands
import datetime
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_PORT = int(MONGO_PORT)
myclient = pymongo.MongoClient(
    f"mongodb://localhost:{MONGO_PORT}", username=USERNAME, password=PASSWORD)
mydb = myclient['smarkbot']


class banlog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):

        mycol = mydb[str(guild.id)]  # collection

        document = mycol.find_one({'_id': member.guild.id})

        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        log_channel = int(document['logsChannellID'])
        channel = self.client.get_channel(log_channel)
        logs = logs[0]
        if logs.target == member:
            await channel.send(f'{logs.user} has just banned {logs.target} (The time is {logs.created_at}), and their reason for doing so is {logs.reason}')

def setup(client):
    client.add_cog(banlog(client))
