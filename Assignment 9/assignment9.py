f=open('sampletext1.txt','r',encoding='utf-8')
txt=f.read().split()
exceptions=['Mr.','Jr.','Ms','Mrs','Dr.']
i=0
new_text=''

new_text.join(exceptions)
# for word in txt:
#     if '?' not in word or '!' not in word:
#         new_text.join(word)
    
        
print(new_text)





