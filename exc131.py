import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
cont = 1
url = 'http://py4e-data.dr-chuck.net/comments_821107.xml'
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
tree = tree.findall('comments/comment/count')
#tree = tree.findall('.//count') ---- También se puede usar esta línea.

while True:
    if not cont <= len(tree):
        break
    x = tree[cont-1]
    num = int(x.text)
    sum = sum + num
    cont = cont + 1

#for x in tree: ----- Este podría ser otra opción más corta y fácil.
    #num = int(x.text)
    #sum = sum + num

print(sum)
