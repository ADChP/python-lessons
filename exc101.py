name = open('mbox-short.txt')
hours = list()
hours2 = list()
count = dict()

for line in name:
    if line.startswith('From '):
        words = line.split()
        hour = words[5]
        hour = hour.split(':')
        hours.append(hour[0])

for hour in hours:
    count[hour] = count.get(hour, 0) + 1

for k,v in count.items():
    hours2.append((k,v))

hours2 = sorted(hours2)

for x,y in hours2:
    print(x,y)
