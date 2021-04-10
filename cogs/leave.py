import discord
from discord.ext import commands
import datetime

class leave(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        who_joined = member
        channel = self.client.get_channel(552215913055911946)
        pfp = who_joined.avatar_url_as(size=32)


        embed_left=discord.Embed(description = f'{who_joined.mention} {who_joined}', color=0xff0000)
        embed_left.set_author(icon_url=pfp, name = 'Member Left')
        embed_left.set_footer(text=f'{who_joined.id}', icon_url=pfp)
        embed_left.add_field(name=f'Account created at: ', value=f'`{str(who_joined.created_at)[:-7]}`', inline=False)
        embed_left.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed_left)

def setup(client):
    client.add_cog(leave(client))
