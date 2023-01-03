from rank import *
from token_config_bot import *
import requests
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

@client.command()
async def rank(ctx, username: str):
	r = requests.get(f'https://api.www.root-me.org/{username}',headers=headers)
	if r.status_code == 200:
		points = get_user_rank(username)
		await ctx.send(f"{username} a {points} points sur Root-Me")
	else:
		await ctx.send('Erreur lors de la récupération des données')

client.run(token)