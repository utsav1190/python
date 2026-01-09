grams = int(input("Enter grams: "))

kg = grams // 1000
remaining_grams = grams % 1000

print(kg, "kg and", remaining_grams, "grams")
