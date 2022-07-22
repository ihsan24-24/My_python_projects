def dividend(name, sales, wastage, amaunt):
    
    sales_devinde = sales - (product[name])
    wast_free = int(amaunt - (amaunt * wastage / 100))
    sales_devinde = sales_devinde * wast_free
    return sales_devinde
product = {"Aplle" : 10 , "Pier": 12, "Domato" : 8, "Pepper" : 20}
lastproduct = {}
for i in list(product.keys()):
    wastage = int(input(f"Enter the estimated waste amount for the {i} : "))
    sales = float(input(f"Enter the selling price for the {i} : "))
    amaunt = int(input(f"Enter the amount of {i} you have : "))
    lastproduct[i] = ["Estimated profit : ", dividend(i, sales, wastage, amaunt), f"estimated amount of waste {int(amaunt * wastage / 100)} KG" ]
    if dividend(i, sales , wastage, amaunt) < 0:
        print("This product was sold at a loss...")
sum = 0
for i in lastproduct:
    sum += lastproduct[i][1]
print(lastproduct)
print("Profit from products : ", sum)

    





