pattern = 0
def shop(money,cart,cost,i):
    if money == 0:
        cart = [str(e) for e in cart]
        print(' '.join(cart))
        global pattern 
        pattern += 1
        return
    elif money < 0 or i>=len(cost):
        return 0
    elif money > 0:
        cart.append(cost[i])
        shop(money-cost[i],cart,cost,i+1)
        cart.pop()
    shop(money,cart,cost,i+1)

money,product = input('Enter Input (Money, Product) : ').split('/')
product = product.split() 
product = [int(e) for e in product]
shop(int(money),[],product,0)

print(f"Krisada can purchase Product: {product} with: {money} Baht | {pattern} Pattern")