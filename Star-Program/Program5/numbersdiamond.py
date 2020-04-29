space=3
num=int(input("Enter the numbers"))
for i in range(0,num):
  for j in range(space-i):
    print(end=" ")
  for j in range(i+1):
    print(i,end=" ")
  print(" ")
number=4
spaces=3
for i in range(0,number):
  for j in range(i+1):
    print(end=" ")
  for j in range(3-i):
    print(i,end=" ")
  print(" ")