courses = ['History', 'math', 'physics', 'comp sci']
course_2 = ['Art', 'Education']
courses.append('Art')
courses.insert(0, 'Music')
# courses.insert(0, course_2)
courses.remove('math')
courses.pop()
popped = courses.pop()
print(popped)

print(courses)
print(len(courses))
print(courses[0])
print(courses[len(courses) - 1])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[0:])
courses_3 = ['History', 'math', 'physics', 'comp sci']
courses_3.extend(course_2) 
print(courses_3)

courses.reverse()
courses.sort()
print(courses)
nums = [1, 5 , 2, 6]
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)

sorted(courses_3)
print(courses_3)

sorted_courses = sorted(courses_3)
print(sorted_courses)

print(min(nums))
print(sum(nums))
print(courses.index('Music')) #To print the index of that value
print('Math' in courses) #To check if a value exists in the list
