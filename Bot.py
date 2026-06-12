import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def guess(ctx):
    await ctx.send("Zgadnij liczbę od 1 do 10")

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit() 
    answer = random.randint(1, 10)

    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Odpowiadasz za długo, prawidłowa odpowiedź to {answer}.')
    if int(guess.content) == answer:
        await ctx.send('Masz rację. Brawo!')
    else:
        await ctx.send(f'Źle! Prawidłowa odpowiedź to {answer}.')

bot.run("")
