#!/usr/bin/python

from rank import get_user_image, get_user_rank, get_user_profile, get_user_last
from token_config_bot import token
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
		embed = discord.Embed(title=username, description="Voici le classement de " + username, color=0x00ff00)
		image_url = get_user_image(username) 
		embed.set_thumbnail(url=image_url)
		points , position, top, challs, comprom = get_user_rank(username)
		embed.add_field(name="Points", value=points, inline=False)
		embed.add_field(name="Position", value=position, inline=False)
		embed.add_field(name="Top", value=top, inline=False)
		embed.add_field(name="Challenges", value=challs, inline=False)
		embed.add_field(name="Compromissions", value=comprom, inline=False)
		await ctx.send(embed=embed)
	else:
		await ctx.send('Erreur lors de la récupération des données')

@client.command()
async def profile(ctx, username: str):
	r = requests.get(f'https://api.www.root-me.org/{username}',headers=headers)
	if r.status_code == 200:
		embed = discord.Embed(title=username, description="Voici le profil de " + username, color=0x00ff00)
		image_url = get_user_image(username) 
		embed.set_thumbnail(url=image_url)
		scores = get_user_profile(username)
		embed.add_field(name="Score", value=scores, inline=False)
		await ctx.send(embed=embed)
	else:
		await ctx.send('Erreur lors de la récupération des données')

@client.command()
async def last(ctx, username: str):
	r = requests.get(f'https://api.www.root-me.org/{username}',headers=headers)
	if r.status_code == 200:		
		embed = discord.Embed(title=username, description="Voici les dernières résolutions de " + username, color=0x00ff00)
		image_url = get_user_image(username) 
		embed.set_thumbnail(url=image_url)
		last = get_user_last(username)
		embed.add_field(name="Challenges", value=last, inline=False)
		await ctx.send(embed=embed)
	else:
		await ctx.send('Erreur lors de la récupération des données')

@client.command()
async def embed(ctx):
	embed = discord.Embed(title="Titre", description="Description", color=0x00ff00)
	embed.add_field(name="Champ 1", value="Valeur 1", inline=False)
	embed.add_field(name="Champ 2", value="Valeur 2", inline=False)
	embed.set_footer(text="Un truc de ce genre")
	await ctx.send(embed=embed)


client.run(token)
