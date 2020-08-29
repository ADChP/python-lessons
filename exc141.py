import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

page = "http://py4e-data.dr-chuck.net/comments_821108.json"
data = urllib.request.urlopen(page, context=ctx).read()
info = json.loads(data)

suma = 0
for item in info['comments']:
    cnt = int(item['count'])
    suma = suma + cnt

print(suma)
