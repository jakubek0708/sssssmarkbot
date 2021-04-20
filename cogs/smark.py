from discord.ext import commands

co_smark = ('śpi', 'spi', 'śpią', 'spia')

smark_spi = False

class smark(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def smark(self, ctx):
        smark_status = 'nie żyje'
        server = self.client.get_guild(id=489137343148851210)
        smark = server.get_member(293079974787678209)
        voice_state = smark.voice

        smark_check = str(smark.status)

        if voice_state is not None:
            smark_spi = any(ext in voice_state.channel.name.lower() for ext in co_smark)
        else:
            smark_spi = False

        if smark_spi:
            smark_status = 'śpi'

        elif smark_check == 'online':
            smark_status = 'żyje'

        elif smark_check == 'offline':
            smark_status = 'nie żyje'

        elif smark_check == 'idle':
            smark_status = 'chyba nie żyje'

        elif smark_check == 'dnd':
            smark_status = 'robo cii'

        await ctx.send(f'stan smarka: {smark_status}')

def setup(client):
    client.add_cog(smark(client))
