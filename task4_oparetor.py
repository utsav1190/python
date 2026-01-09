
amount = int(input("Enter amount in rupees: "))

denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for d in denominations:
    count = amount // d
    if count > 0:
        value = d * count
        print(f"{d} x {count} = {value:>3}")
        amount = amount % d
