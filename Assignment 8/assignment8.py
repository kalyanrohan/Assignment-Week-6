f=open('POKEMON.txt','r',encoding='utf-8')
txt=f.read().split()
pokemon_dict = {}

for names in txt:
    if names[0] not in pokemon_dict:
        pokemon_dict[names[0]] = [names]
    else:
        pokemon_dict[names[0]].append(names)

longest_count = 0
longest_chain = []

def longest_name(chain):
    global longest_count
    global longest_chain

    #Longest checking
    if len(chain) > longest_count:
        longest_count = len(chain)
        longest_chain = chain

    # The code snippet to find the next value in the chain
    if chain[-1][-1] in pokemon_dict:
        for name in pokemon_dict[chain[-1][-1]]:
            if name not in chain:
                longest_name(chain + [name])
        
for names in txt:
    longest_name([names])

print(f"{longest_chain} length: {longest_count}")
