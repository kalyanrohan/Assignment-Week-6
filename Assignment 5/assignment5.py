from collections import defaultdict
dict1=defaultdict(int)
with open ('sampletext.txt','r') as f:
    txt=f.read()
    txt.split(" ",",",".","?","!",":",)
print(txt)



