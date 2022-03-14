import requests
from bs4 import BeautifulSoup

def parsingweb():
    websiteurl = "https://www.felixfaal.com"
    requestAPI = requests.get(websiteurl)
    somethingtoadd = requestAPI.text
    print(somethingtoadd)

parsingweb()
