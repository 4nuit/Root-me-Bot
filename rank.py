#!/usr/bin/python

import time
import requests
import re

# User Agent lambda pour pas avoir de 429

def get_user_rank(username):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	api_url = f"https://api.www.root-me.org/user/{username}"
	response = requests.get(api_url, headers=headers)
	if response.status_code == 200:
		#print(response.text)
		pattern_points = r"<h3><img src='squelettes/img/valid.svg\?\d+' width='\d+' height='\d+' />&nbsp;(\d+)</h3>"
		points = re.search(pattern_points, response.text).group(1)
		time.sleep(0.2)  # Délai entre chaque requête
		
		pattern_rank = r"<h3><img src='squelettes/img/classement.svg\?\d+' width='\d+' height='\d+' />&nbsp;(\d+)</h3>"
		rank = re.search(pattern_rank, response.text).group(1); print(rank)

		return points, rank
	else:
		time.sleep(0.2)  # Délai entre chaque requête
		return "Error retrieving user ranking"

# Exemple d'utilisation
#username = ""
#points , rank = get_user_rank(username)
#print(f"{username} a {points} points et est classé {rank} sur Root-Me")
