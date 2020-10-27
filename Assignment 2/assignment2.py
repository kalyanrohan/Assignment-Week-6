prices= {"banana": [4,12],
"apple": [2,0],
"orange": [1.5,10],
"pear": [3,5]
}


for key in prices:
    print(key)
    print(f'price: ${prices[key][0]}')
    print(f'stock: {prices[key][1]}')

total=0
for key in prices:
    result=prices[key][0]*prices[key][1]
    total=total+result
print(f'total: ${total}')
