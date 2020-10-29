f=open('sampletext1.txt','r',encoding='utf-8')
txt=f.read().split()
exceptions=['Mr.','Jr.','Ms.','Mrs.','Dr.']
print(txt)
new_text=''
for word in txt:
    if '?' not in word and '!' not in word:
        new_text+=(word + " ")
        if '.' in word.strip('.') and word not in exceptions:
            pass
        elif '.' in word[-1] and word not in exceptions:
            new_text+="\n"
    else:
        new_text+=(word + "\n")

print(new_text)   






