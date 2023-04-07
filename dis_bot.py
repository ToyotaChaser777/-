import discord
from discord.ext import commands
from bot_logic import gen_pass

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def привет(ctx):
    await ctx.send(f'{ctx.message.author.mention}, Привет!')

@client.command()
async def хелп(ctx):
    await ctx.send('Я бот, да ты и сам знаешь.\n**Мои команды:**\n```!привет - Вывод сообщения с приветом.``` ```!хелп - эта команда.``` ```!пароль (кол-во символов) - генератор паролей.```')

@client.command()
async def пароль(ctx, number: int):
    await ctx.send(gen_pass(number))


client.run("Token")
