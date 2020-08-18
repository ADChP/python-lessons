text = "X-DSPAM-Confidence:    0.8475"
ext1 = text.find('0.84')
ext2 = text[ext1:]
ext3 = float(ext2)
print(ext3)
