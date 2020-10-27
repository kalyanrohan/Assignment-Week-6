from collections import defaultdict
dict1=defaultdict(int)
f=open ('sampletext.txt','r')
txt=f.read().split()
new_txt=[]
for word in txt:
    new_txt.append(word.strip('!.:;,?-/_$%()'))

for word in new_txt:
    dict1[word]+=1

hapaxes=[]

for word,count in dict1.items():
    if count==1:
        hapaxes.append(word)
print(hapaxes)
print(len(hapaxes))
print(len(new_txt))



