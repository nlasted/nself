from discord.ext import commands

class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True)
    async def hello_world(self, ctx):
        await ctx.send("Hello, World!")

async def setup(bot):
    await bot.add_cog(HelloWorld(bot))