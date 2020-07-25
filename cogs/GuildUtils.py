import datetime as dt
import time

import discord
from discord.ext import commands


class GuildUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx):
        embed = discord.Embed(
            title=":newspaper: @ekko",
            description="""Hello World""",
            color=0xd6b360,
            timestamp=dt.datetime.utcfromtimestamp(time.time())
        )
        await ctx.send(embed=embed)


def setup(bot):
    print('GuildUtils loaded')
    bot.add_cog(GuildUtils(bot))
