f=open('POKEMON.txt','r',encoding='utf-8')
txt=f.read().split()

pokemon_dict={}

for names in txt:
    if names[0] not in pokemon_dict:
        pokemon_dict[names[0]] = [names]
    else:
        pokemon_dict[names[0]].append(names)



