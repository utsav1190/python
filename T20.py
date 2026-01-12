#Given two lists, convert them into sets and find common elements.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Find common elements
common_elements = set1 & set2   # or set1.intersection(set2)

print(common_elements)
