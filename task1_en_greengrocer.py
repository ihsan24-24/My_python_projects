""" Task : A greengrocer will buy products from a wholesale vegetable store. Products can be purchased in certain quantities and multiples.
For example, apples can be sold in 10 kg and its multiples. If you want 12 kilos of apples, you can gain 10 kilos, or if you want 22 kilos, you can gain 20 kilos.
The greengrocer enters her budget and according to her budget, the kilogram price of the product she/he wants is calculated starting from the most expensive.
She/he can buy as much product as budget. And finally, the money is calculated and returned. """
product = {"Apple" : [10,10] , "Pier": [12,5], "Domato" : [8,20], "Pepper" : [20, 4]} 
received = {}
productlast = []
print("""Product      wholesale price   available weight and multiples
-----------------------------------
Apple      $ 10            KG 10
Pier     $ 12            KG 5 
Domato   $ 8             KG 20
Pepper     $ 20            KG 4 """)
budget = int(input("What's your budget for shopping? : "))
remainder = budget 
for i in list(product.keys()):
    wanted = int(input(f"Enter the amount you want to buy from the {i} product : "))
    productlast.append([i, product[i][0], (wanted - (wanted % product[i][1]))])
productlast.sort(reverse = True , key= lambda x: x[1])
for i in range(len(productlast)):
    price = productlast[i][1] * productlast[i][2]
    if (remainder >= price) and (price != 0):
        remainder -= price
        received[productlast[i][0]] = [f"price : {price} $", f" amaunt : {productlast[i][2]} KG"]

if len(received) == 0:
    print("Your budget is insufficient or you have not entered a product...")
else:
 print(received)
 print("Total fee payable : ", budget - remainder, " $  Over money : ", remainder, " $" )