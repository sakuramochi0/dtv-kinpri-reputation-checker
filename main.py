import datetime
import sys

import requests
from bs4 import BeautifulSoup

url = 'https://pc.video.dmkt-sp.jp/ti/10020330'

try:
    r = requests.get(url)
except:
    sys.exit(1)
soup = BeautifulSoup(r.text, 'html.parser')

time = datetime.datetime.now()
star = soup.select('.ratingStar_number')[0].text

print(','.join([str(time), star]))
