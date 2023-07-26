
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}



print(student)
print(student['name'])
print(student['courses'])
# print(student['phone']) It shows an erron
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student['phone'] = '555-2515'
print(student.get('phone'))

student.update({'name': 'Jane'})
print(student)

del student['age']
print(student)

name = student.pop('name')
print(student)
print(name)	

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
	print(key) #will only loop throgh keys

for key, value in student.items():
	print(key, value)
