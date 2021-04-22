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

        smark_spi = voice_state is not None and voice_state.channel.category_id == 833937577853059073

        smark_status_dict = {
            'online': 'żyje',
            'offline': 'nie żyje',
            'idle': 'chyba nie żyje',
            'dnd': 'robo cii'
        }

        if smark_spi:
            smark_status = 'śpi'
        else:
            smark_status = smark_status_dict[smark_check]

        await ctx.send(f'stan smarka: {smark_status}')


def setup(client):
    client.add_cog(smark(client))
