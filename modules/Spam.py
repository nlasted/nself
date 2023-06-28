import random
import asyncio
from discord.ext import commands

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def spam(self, ctx, times, *, msg):
        await ctx.message.delete()
        for i in range(int(times)):
            await ctx.send(msg)
            await asyncio.sleep(0.2)

async def setup(bot):
    await bot.add_cog(Spam(bot))