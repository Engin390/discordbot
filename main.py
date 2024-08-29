import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bb(ctx):
    await ctx.send('Sonra görüşürüz!!')

@bot.command()
async def areyouapopularbot(ctx):
    await ctx.send('No, But My Creator Is Trying To Make Me Popular lol')

@bot.command()
async def nasılsın(ctx):
    await ctx.send('daha iyi olamazdım')

@bot.command()
async def acıktım(ctx):
    await ctx.send('gel de beni ye!')

bot.run("burayatoken")
