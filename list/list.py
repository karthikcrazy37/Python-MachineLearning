#creating the list
courses=['physics','maths','chemistry','computer']
print(courses)
#adding values
courses.append("English")
print(courses)
courses.insert(0,"Tamil")
print(courses)
#deleting values
courses.remove('physics')
print(courses)
popped=courses.pop()
print(popped)
#sorting elements
nums=[1,4,5,8,6,2]
nums.sort()
print(nums)
#sorting in descending order
nums.sort(reverse=True)
print(nums)
#using index values
courses[0:2]
print(courses.index("chemistry"))
print(courses)
#finding min max values and sum
print(min(nums))
print(max(nums))
print(sum(nums))