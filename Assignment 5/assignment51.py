dict1={}
f=open('sampletext2.txt','r',encoding='utf-8')
txt=f.read().split()
new_txt=[]
for word in txt:
    w1=word.strip('!.:;,?-/_$%()').lower()
    new_txt.append(w1)


def hapax(txt):
    for word in txt:
        if word in dict1:
            dict1[word]+=1
        else:
            dict1[word]=1
    hapaxes=[]
    for word,count in dict1.items():
        if count==1:
            hapaxes.append(word)
    return hapaxes

print(hapax(new_txt))
