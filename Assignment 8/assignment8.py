f=open('POKEMON.txt','r',encoding='utf-8')
txt=f.read().split()
print(txt)
pokemon_dict= {}
longest_chain=[]
for name in pokemon_dict:
    if name[0] not in pokemon_dict:
        pokemon_dict[name[0]] = [name]
    else:
        pokemon_dict[name[0]].append(name)
print(pokemon_dict)


