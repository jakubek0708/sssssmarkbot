from discord.ext import commands
import discord 

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test failed damb")

        class Counter(discord.ui.View):
            @discord.ui.button(label='0', style=discord.ButtonStyle.red)
            async def counter(self, button: discord.ui.Button, interaction: discord.Interaction):
                number = int(button.label)
                button.label = str(number + 1)
                if number + 1 >= 5:
                    button.style = discord.ButtonStyle.green

                await interaction.message.edit(view=self)

        view = Counter()
        await ctx.send('Press to increment', view=view)

def setup(client):
    client.add_cog(test(client))
