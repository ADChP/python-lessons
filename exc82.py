fname = 'mbox-short1.txt'
fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From '):
        line = line.split()
        print(line[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
