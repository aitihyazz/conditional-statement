costprice=int(input("Enter the CP:"))
sellingprice=int(input("Enter the SP:"))
if sellingprice>costprice:
    print("profit")
    pt=sellingprice-costprice
    print(pt)
else :
    print("No profit")