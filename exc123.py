from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = "http://py4e-data.dr-chuck.net/known_by_Tia.html"
cont = 7
line = 18

print('Retrieving: %s' % link)
for i in range(0, cont):
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    ps = 0

    for tag in tags:
        ps += 1
        if ps == line:
            print('Retrieving:', tag.get('href', None))
            link = tag.get('href', None)
            ps = 0
            break
