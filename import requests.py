import requests
from bs4 import BeautifulSoup

def parsingweb():
    websiteurl = "https://www.felixfaal.com"
    requestAPI = requests.get(websiteurl)
    webtext = requestAPI.text
    print(webtext)

parsingweb()
