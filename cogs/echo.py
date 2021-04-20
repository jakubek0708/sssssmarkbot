from discord.ext import commands

smarkbot_staff = (390956680705474571,
                  386209774481571841,
                  293079974787678209,
                  226646760515305473,
                  294936820595163142,
                  288028423031357441,
                  265085929809510402)

class echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, message):
        if ctx.message.author.id in smarkbot_staff:
            await ctx.message.delete()
            await ctx.send(message)

def setup(client):
    client.add_cog(echo(client))
