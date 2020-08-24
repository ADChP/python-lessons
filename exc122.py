from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_821105.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
suma = 0
for tag in tags:
    suma = suma + int(tag.contents[0])
    # Look at the parts of a tag
    #'TAG:', tag
    #'URL:', tag.get('href', None)
    #'Contents:', tag.contents[0]
    #'Attrs:', tag.attrs

print(suma)
