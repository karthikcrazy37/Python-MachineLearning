def InsertionSort(my_list):
  for index in range(1,len(my_list)):
    current_element=my_list[index]
    pos=index
    while current_element<my_list[pos-1] and pos>0:
      my_list[pos]=my_list[pos-1]
      pos=pos-1
    my_list[pos]=current_element
list1=[3,4,5,6,1,2]
InsertionSort(list1)
print(list1)