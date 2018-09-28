# Work with Python 3.6
import discord
from discord.ext import commands
import localtoken

TOKEN = localtoken.LOCALTOKEN

bot = commands.Bot(command_prefix='$')

@bot.command()
async def greet(ctx):
    
    msg = 'Hello {0.author.mention}! :wave:'.format(ctx)
    await ctx.send(msg)

@bot.command()
async def math(ctx, a: int, arg, b: int):

    if (arg == '*'):
        await ctx.send(a * b)
    elif (arg == '+'):
        await ctx.send(a + b)
    elif (arg == '-'):
        await ctx.send(a - b)
    elif (arg == '/'):
        await ctx.send(a // b)
    else:
        await ctx.send("Sorry {0.author.mention}, that command isn't something I can do!".format(ctx))
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)