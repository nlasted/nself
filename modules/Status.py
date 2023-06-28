import os
import discord
import platform
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True)
    async def status(self, ctx, status_name):
        await ctx.message.delete()
        match(status_name):
            case "dnd":
                await self.bot.change_presence(status = discord.Status.dnd)
            case "on":
                await self.bot.change_presence(status = discord.Status.online)
            case "idle":
                await self.bot.change_presence(status = discord.Status.idle)
            case "off":
                await self.bot.change_presence(status = discord.Status.offline)

    @commands.command(pass_context = True)
    async def self(self, ctx):
        data = platform.freedesktop_os_release()
        name = data['NAME']
        version = data['VERSION']
        architecture = platform.machine()
        shell = os.environ['SHELL']
        username = os.environ['USER']
        await ctx.message.delete()
        await ctx.send(f"# OS Info + Status\n:ping_pong: Ping: {round(self.bot.latency *1000)}ms\n:desktop: OS: {name} {version} {architecture}\n:person_frowning: Username: {username}\n:shell: Shell: {shell}")
    

async def setup(bot):
    await bot.add_cog(Status(bot))