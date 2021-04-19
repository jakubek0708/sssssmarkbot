from discord.ext import commands

class smark(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def smark(self, ctx):
        smark_status = 'nie żyje'
        server = self.client.get_guild(id=489137343148851210)
        smark = server.get_member(293079974787678209)
        voice_state = smark.voice

        if voice_state is not None:
            if voice_state.channel.id == 831675365738545162:
                smark_status = 'śpi'
                
        elif smark.status == 'online':
            smark_status = 'żyje'

        elif smark.status == 'offline':
            smark_status = 'nie żyje'

        elif smark.status == 'idle':
            smark_status = 'chyba nie żyje'

        elif smark.status == 'dnd':
            smark_status = 'coś robi cii'

        await ctx.send(f'stan smarka: {smark_status}')

def setup(client):
    client.add_cog(smark(client))
