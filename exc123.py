from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
inic = 2
fin = 4
fin = fin + 1

while fin != 0 :
    page = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(page, "html.parser")
    tags = soup('a')[inic]
    tags = tags.get('href', None)
    fin = fin - 1
    inic = inic + 1
    print(tags)
