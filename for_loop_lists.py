
courses = ['History', 'math', 'physics', 'comp sci']

for index, item in enumerate(courses, start = 1):
	print(index, item)

for item in enumerate(courses):
	print(item)

for item in enumerate(courses, start = 1):
	print(item)	

for item in (courses):
	print(item)

course_str = ', '.join(courses)

print(course_str)

new_list = course_str.split(', ')
print(new_list)
