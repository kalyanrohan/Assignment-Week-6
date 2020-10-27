stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
groceries=["banana","orange","apple"]
def compute_bill(food):
    total=0
    for item in food:
        if stock[item]>0:
            total_price_of_item=prices[item]*stock[item]
            total+=total_price_of_item
            stock[item]-=1 
    return total

print(f'Your total is: ${compute_bill(groceries)}')
print(stock['banana'])
