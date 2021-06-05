from discord.ext import commands

smarkbot_staff = (390956680705474571,  # toxic
                  386209774481571841,  # haav
                  293079974787678209,  # smark
                  226646760515305473,  # witt
                  288028423031357441,  # zniks
                  265085929809510402,  # maggo
                  294936820595163142,  # bigos
                  376823160365907981)  #kitkat


class echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, message):
        if ctx.message.author.id in smarkbot_staff:
            if '@everyone' in message: 
                return await ctx.send('Ty kurwa dziwko jebana co chcesz everyone pingować, wypierdalaj')
            await ctx.message.delete()
            await ctx.send(message)


def setup(client):
    client.add_cog(echo(client))
