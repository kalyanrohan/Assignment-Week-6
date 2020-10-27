f=open('sampletext2.txt','r',encoding="utf-8")
new_file=open('new_file.txt','w',encoding="utf-8")
txt=f.readlines()
i=1
for line in txt:
    new_file.write(f'{i}.{line}')
    i+=1
    

    
