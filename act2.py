costprice =int(input("enter the cp: "))
sellingprice =int(input("enter the sp: "))

if(sellingprice>costprice):
    print("profit")
    pt=sellingprice-costprice
    print(pt)
else :
    print("no profit, loss")
    pt=sellingprice-costprice
    print(pt)