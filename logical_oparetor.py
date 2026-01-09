#logical oparetor
num1=int(input("Enter first number="))
num2=int(input("Enter second number"))
num3=int(input("Enter thared number"))

print(num1)
print(num2)
print(num3)

#LOGICAL and oparetor

result = num1 <num2 and num2 <num3
print(f'{result} = {num1} <{num2} and {num2} <{num3}')

#LOGICAL or oparetor

result = num1 <num2 or num2 <num3
print(f'{result} = {num1} >{num2} or {num2} >{num3}')

#LOGICAL not oparetor

result = not(num1 <num2 or num2 <num3)
print(f'{result} =  not {num1} <{num2} and {num2} <={num3}')