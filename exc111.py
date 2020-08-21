import re

data = open('regex_sum_821103.txt')
numbers = list()

for line in data:
    x = re.findall('[0-9]+', line)
    if len(x) < 1:
        continue
    for y in x:
        num = int(y)
        numbers.append(num)

print(sum(numbers))
