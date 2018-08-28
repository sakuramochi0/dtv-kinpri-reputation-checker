import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://pc.video.dmkt-sp.jp/ti/10020330'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

time = datetime.datetime.now()
star = soup.select('.ratingStar_number')[0].text

print(','.join([str(time), star]))