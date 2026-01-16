purches_price=float(input("Entre purches price="))
selling_price=float(input("Enter Selling price="))
Diffrence=selling_price-purches_price
if Diffrence>0:
    print('Profit is',Diffrence)
if Diffrence<0:
    print('Loss is',Diffrence)
if Diffrence==0:
    print('No Profit No Loss')
