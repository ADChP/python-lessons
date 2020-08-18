doc = open('mbox-short.txt')
contacts = dict()
maxvalue = None
maxkey = None

for line in doc:
    if not line.startswith('From '):
        continue
    else:
        word = line.split()
        mail = word[1]
        contacts[mail] = contacts.get(mail,0)+1

for k,v in contacts.items():
    if maxvalue is None or v > maxvalue:
        maxvalue = v
        maxkey = k

print(maxkey, maxvalue)
