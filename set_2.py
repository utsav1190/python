set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1,set2)
#get unique valule from both set (no repitation)
set3=set1.union(set2)
print(set3)
#get common values from both set
set4=set1.intersection(set2)
print(set4)
#get all values that is in one(set1)setbut not in other set(set2)
set5=set1.difference(set2)
print(set5)

#create a list that has duplicate valuse
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers)
print(len(numbers))
#remove all duplicate values
