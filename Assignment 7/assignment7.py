f=open('sampletext2.txt','r',encoding='utf-8')
txt=f.read().split()
new_text=[]
for word in txt:
    new_text.append(word.strip('!,.:;()$@%&/='))

def average_word_length(word_list):
    total=0
    for word in word_list:
        total+=len(word)
    ave=total/len(word_list)
    return ave


print(f'average word length: {average_word_length(new_text)}')

