import os
import json
import logging
from discord.ext import commands

if (os.path.isfile("conf.json") == False):
    print("No configuration detected.")
    token_input = input("Enter discord token: ")
    prefix_input = input("Enter prefix: ")
    Raw_Config = {"token": token_input, "prefix": prefix_input}
    f = open("conf.json", "w")
    f.write(json.dumps(Raw_Config, sort_keys=True, indent=4))
    f.close()

with open("conf.json", "r") as config_file:
    config = json.loads(config_file.read())

handler = logging.FileHandler(filename='nself.log', encoding='utf-8', mode='w')

bot = commands.Bot(command_prefix=config["prefix"], self_bot=True)

@bot.event
async def setup_hook():
    os.system("clear")
    print("""
               _  __ 
  _ _  ___ ___| |/ _|
 | ' \(_-</ -_) |  _|
 |_||_/__/\___|_|_|
 """)
    errors = 0
    print("┏ 󰦖 Loading modules...")
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'modules.{filename[:-3]}')
                print(f"┃  Loaded module: {filename[:-3]}")
            except Exception as module_failure:
                print(f"┃  Failed to load module: {filename[:-3]}")
                f = open(f"{filename[:-3]}.exception", "w")
                f.write(str(module_failure))
                f.close()
                errors += 1
    if (errors >= 1):
        print(f"┗  Loaded! Errors: {errors}")
    else:
        print(f"┗  Fully loaded!")

@bot.command()
async def reload(ctx, module):
    await ctx.message.delete()
    try:
        await bot.unload_extension(f'modules.{module}')
        await bot.load_extension(f'modules.{module}')
        await ctx.send(f":white_check_mark: Reloaded **{module}**.")
    except:
        await ctx.send(f":x: Failed to reload **{module}**.\n- Double check module for errors and reload again.\n- If you see this message again module might not exist.")

@bot.command()
async def reload_all(ctx):
    await ctx.message.delete()
    await ctx.send(":hourglass: Reloading all modules...")
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            try:
                await bot.unload_extension(f'modules.{filename[:-3]}')
                await bot.load_extension(f'modules.{filename[:-3]}')
                await ctx.send(f":white_check_mark: Loaded **{filename[:-3]}**.")
            except:
                await ctx.send(f":warning: Failed to load **{filename[:-3]}**.")
    await ctx.send("**:ok_hand: Reload complete**")

bot.run(config["token"], log_handler=handler)