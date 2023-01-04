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
		pattern = r"<h3><img src='squelettes/img/valid.svg\?\d+' width='\d+' height='\d+' />&nbsp;(\d+)</h3>"
		points = re.search(pattern, response.text).group(1)
		time.sleep(1)  # Ajoutez un délai d'une seconde entre chaque requête
		return points
	else:
		time.sleep(1)  # Ajoutez un délai d'une seconde entre chaque requête
		return "Error retrieving user ranking"

# Exemple d'utilisation
#username = ""
#points = get_user_rank(username)
#print(f"{username} a {points} points sur Root-Me")
