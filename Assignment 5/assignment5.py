from collections import defaultdict
dict1=defaultdict(int)
f=open('sampletext2.txt','r')
txt=f.read().split()
new_txt=[]
for word in txt:
    w1=word.strip('!.:;,?-/_$%()').lower()
    new_txt.append(w1)

for word in new_txt:
    dict1[word]+=1

hapaxes=[]
print(dict1.items())
for word,count in dict1.items():
    if count==1:
        hapaxes.append(word)
print(hapaxes)
print(len(hapaxes))
print(len(new_txt))

# 5182
# 78256

