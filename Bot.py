import discord
from discord.ext import commands
import random
import asyncio
import os
import requests


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
@bot.command()
async def games(ctx):
    
    links = ["https://marcelixon12.itch.io/the-power-of-ring"]
    game = random.choice(links)
    
    await ctx.send(game)
@bot.command()
async def info(ctx):
    commands = ['$hello', '$heh', '$guess', '$info', '$games', '$editme', '$mem', '$duck', '$dog' ]
    explaines = ['Bot przywita się z tobą', 'Po $heh możesz dodać jakąś liczbę, a bot napisze he tyle razy ile to napisałeś, jeśli nic nie napiszesz bot wypisze he 5 razy', 'Musisz zgadnąć cyfrę od 1 do 10', 'Wyświetla wszystkie komendy', 'Wyświetla linki do gier twórcy', 'Jeśli wpiszesz po niej słowo bot je zedytuje', 'Wysyła fajne memy', 'Wysyła zdjęcie kaczki', 'Wysyła zdjęcia lub filmy z psami']
    await ctx.send(commands[0])
    await ctx.send(explaines[0])
    await ctx.send(commands[1])
    await ctx.send(explaines[1])
    await ctx.send(commands[2])
    await ctx.send(explaines[2])
    await ctx.send(commands[3])
    await ctx.send(explaines[3])
    await ctx.send(commands[4])
    await ctx.send(explaines[4])
    await ctx.send(commands[5])
    await ctx.send(explaines[5])  
    await ctx.send(commands[6]) 
    await ctx.send(explaines[6]) 
    await ctx.send(commands[7]) 
    await ctx.send(explaines[7]) 
    await ctx.send(commands[8]) 
    await ctx.send(explaines[8])
    await ctx.send(commands[9]) 
    await ctx.send(explaines[9])
@bot.command()
async def editme(ctx, text = '10'):
    msg = await ctx.send(text)
    await asyncio.sleep(3.0)
    await msg.edit(content= text + '. Super wiadomość')
@bot.command()
async def mem(ctx):

    path = "D:\\GitHub\\Python\\M1L3\\images"

    lista_plikow = os.listdir(path)

    random_mem = random.choice(lista_plikow) 

    sciezka_do_mema = path + "\\" + random_mem

    with open(sciezka_do_mema, 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    
    image_url = get_duck_image_url()
    await ctx.send(image_url)
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    

bot.run("")
