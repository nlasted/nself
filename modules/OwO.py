import uwuify
from discord.ext import commands

flags = uwuify.SMILEY | uwuify.YU | uwuify.STUTTER

class OwO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def owoify(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(uwuify.uwu(text, flags=flags))

async def setup(bot):
    await bot.add_cog(OwO(bot))