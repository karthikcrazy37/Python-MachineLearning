num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
print("Enter 1 for +")
print("Enter 2 for -")
print("Enter 3 for *")
print("Enter 4 for /")
n=int(input("Enter your operator"))
if n==1:
  print(num1+num2)
elif n==2:
  print(num1-num2)
elif n==3:
  print(num1*num2)
elif n==4:
  print(num1/num2)
else:
  print("operator not found")