space=3
num=4
for i in range(0,num):
  for j in range(space-i):
    print(end="")
  for j in range(4-i):
    print("*",end=" ")
  print(" ")