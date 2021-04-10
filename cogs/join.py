import discord
from discord.ext import commands
import datetime

slownik = {}
who_joined = None
send_verification_messages_ids = {}
member_joined_dict = {}

class join(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        global embed_send, who_joined

        who_joined = member

        channel = self.client.get_channel(552215913055911946)

        pfp = member.avatar_url_as(size=32)

        embed=discord.Embed(description = f'{member.mention} {member}', color=0xf28500)
        embed.set_author(icon_url=pfp, name = 'Member Joined')
        embed.set_footer(text=f'{member.id}', icon_url=pfp)
        embed.add_field(name='User verification pending', value=f'Account created at: `{str(member.created_at)[:-7]}`', inline=False)
        embed.timestamp = datetime.datetime.utcnow()

        embed_send = await channel.send(embed=embed)

        send_verification_messages_ids[embed_send.id] = embed_send

        member_joined_dict[embed_send.id] = who_joined

        slownik[embed_send.id] = member

        await embed_send.add_reaction('✅')
        await embed_send.add_reaction('❌')

        print(send_verification_messages_ids)

def setup(client):
    client.add_cog(join(client))
