#!/usr/bin/env python3

import json
import sys
import requests

from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs4

# Los tipos de archivo
TYPE_FOLDER = 'd'
TYPE_FILE   = 'f'

def get_download(link: str) -> str:
	new_content = requests.get(link).content
	bs4_parsed = bs4(new_content, "lxml")
	return bs4_parsed.find("a", {"id":"downloadButton"})["href"]

if (len(sys.argv) < 3):
	print("Sintaxis: %s <Tipo de archivo> <Identificador de la carpeta o dirección URL>" % (sys.argv[0]))
	sys.exit(1)
else:
	type = sys.argv[1].lower()
	id = sys.argv[2]

if (type == TYPE_FILE):
	link = id
	link_info = urlparse(link)
	link2check = link_info.netloc.lower()

	if (link2check != "mediafire.com") and (link2check != "www.mediafire.com"):
		print("Error, el nombre del sitio web al que intenta acceder no coincide con el correspondiente.")
		sys.exit(1)

	print(get_download(link))

elif (type == TYPE_FOLDER):
	folder_key = id
	content = requests.get("https://www.mediafire.com/api/1.4/folder/get_content.php?r=rgfa&content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=%s&response_format=json" % (folder_key)).content
	content_js = json.loads(content)
	parsed = content_js["response"]
	status = parsed["result"]

	if (status != "Success"):
		print("Ocurrió una incongruencia:", status)
		sys.exit(1)

	files = parsed["folder_content"]["files"]
	for file in files:
		link = get_download(file["links"]["normal_download"])
		print(link)

else:
	print("Tipo de archivo desconocido.")
