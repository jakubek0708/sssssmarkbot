import discord
from discord.ext import commands

bot_snowflake = 822169790801641474


class reaction_remove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        from .reaction import troll_messages
        if str(reaction.emoji) == '<:sus:820070011070185503>' and user.id != bot_snowflake and reaction.message.id in troll_messages:
            await reaction.message.remove_reaction('<:trollcrazy:800421758099783710>', user.guild.get_member(bot_snowflake))
            troll_messages.remove(reaction.message.id)


def setup(client):
    client.add_cog(reaction_remove(client))
