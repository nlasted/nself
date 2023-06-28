from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        username_raw = self.bot.user
        username = str(username_raw).split("#")
        print(f"\n󱜙 Self-Bot ready!\nRunning on account  {username[0]}")

async def setup(bot):
    await bot.add_cog(Events(bot))