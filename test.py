import requests
import re
from PIL import Image
from io import BytesIO

username = "macz"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get("https://api.www.root-me.org/user/"+username, headers=headers)
pattern_image = r'<img class="vmiddle logo_auteur logo_6forum" width="[0-9]+" height="[0-9]+" src="(.*)" alt="'+username+'" '
image = re.search(pattern_image, response.text).group(1)
imagetext = "https://www.root-me.org/"+image
print(imagetext)

def show_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.show()

show_image(imagetext)