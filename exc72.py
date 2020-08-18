fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    line = line.strip(":")
    num = line.find(":")
    num = line[num+1:]
    num = float(num.strip())
    sum = sum + num
mean = sum / count
print("Average spam confidence:", mean)
