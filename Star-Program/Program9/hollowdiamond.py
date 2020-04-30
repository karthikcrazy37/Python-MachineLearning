
space=3
num=4
for i in range(0,num):
  for j in range(space-i):
    print(end=" ")
  for j in range(i+1):
    if j==0 or i==j:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print(" ")
number=3
for i in range(0,number):
  for j in range(i+1):
    print(end=" ")
  for j in range(3-i):
    if j==0 or 2-i==j:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print(' ')