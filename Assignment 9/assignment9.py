f=open('sampletext1.txt','r',encoding='utf-8')
txt=f.read().split()
exceptions=['Mr.','Jr.','Ms','Mrs','Dr.']
i=0


for word in txt:
    new_txt=txt[i]
    if "?" not in word or "!" not in word:
        new_txt.join(word)
        i+=1
        
print(new_txt)





