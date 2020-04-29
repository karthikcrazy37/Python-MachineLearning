space=3
num=4
for i in range(0,num):
  for j in range(space):
    print(end="")
  for j in range(i+1):
    print("*",end=" ")
  print(" ")