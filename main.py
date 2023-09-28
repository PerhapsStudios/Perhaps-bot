import discord 
from discord.ext import commands 

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="/", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="help command (Custom)", description="'!ping' - View the ping of the bot", color=discord.color.blue())
  await ctx.channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.reply("pong!")

@bot.command()
async def smell(ctx):
    await ctx.reply("You stink!")
