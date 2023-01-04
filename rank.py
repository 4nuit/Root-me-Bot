#!/usr/bin/python

import time
import requests
import re

# User Agent lambda pour pas avoir de 429
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_user_rank(username=None):
	response = requests.get(f"https://api.www.root-me.org/user/{username}", headers=headers)
	if response.status_code == 200:
		pattern_points = r"<h3><img src='squelettes/img/valid.svg\?\d+' width='\d+' height='\d+' />&nbsp;(\d+)</h3>"
		points = re.search(pattern_points, response.text).group(1)
		time.sleep(0.2)  # Délai entre chaque requête
		
		pattern_rank = r"<h3><img src='squelettes/img/classement.svg\?\d+' width='\d+' height='\d+' />&nbsp;(\d+)</h3>"
		rank = re.search(pattern_rank, response.text).group(1)

		return points, rank
	else:
		time.sleep(0.2)  # Délai entre chaque requête
		return "Error retrieving user ranking"

def get_user_profile(username=None):
	scores = []
	categories = ["Web-Client","Programmation","Cryptanalyse","Steganographie","Web-Serveur","Cracking","Realiste","Reseau","App-Script","App-Systeme","Forensic"]
	response = requests.get(f"https://api.www.root-me.org/user/{username}", headers=headers)
	if response.status_code == 200:
		for category in categories:
			pattern_category = r'href="fr/Challenges/'+category+'/">(\d+)%</a></span>'
			score_category = re.search(pattern_category, response.text).group(1)
			scores.append(category+': '+str(score_category)+"%")
			time.sleep(0.1)  # Délai entre chaque requête

		return scores
	else:
		time.sleep(0.2)  # Délai entre chaque requête
		return "Error retrieving user ranking"

def get_user_last(username=None):
	response = requests.get(f"https://api.www.root-me.org/user/{username}", headers=headers)
	if response.status_code == 200:
		pattern = r';&nbsp;<a href="fr/Challenges/(.+?)/(.+?)"'
		challenges = []
		
		for match in re.finditer(pattern, response.text):
			#1er groupe de capture
			challenge_category = match.group(1)
			#2nd groupe de capture
			challenge_name = match.group(2)
			challenges.append([challenge_category + ': ' + challenge_name])
			time.sleep(0.1)  # Délai entre chaque requête

		returnchallenge = ""
		for challenge in challenges:
			returnchallenge += challenge[0] + "\n"

		return returnchallenge
	
	else:
		time.sleep(0.2)  # Délai entre chaque requête
		return "Error retrieving user ranking"

# Exemple d'utilisation
#username = "Nu1t"
#points , rank = get_user_rank(username)
#print(f"{username} a {points} points et est classé {rank} sur Root-Me")
#scores = get_user_profile(username)
#print(scores)
#challenges = get_user_last(username)
#print(challenges)
