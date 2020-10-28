f=open('sampletext2.txt','r',encoding='utf-8')
txt=f.read().split()
chars = ',./<>!@#$%^&*()-=+{}[]|;?"'

def average_word_length(word_list):
    total = 0
    for word in word_list:
        word.strip(chars)
        for letter in word:
            if letter not in chars:
                total += 1
    return total/len(word_list)

f.close()


print(f'average word length: {average_word_length(txt)}')

