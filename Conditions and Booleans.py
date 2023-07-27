
if True:
	print('Conditional was true')

if False:
	print('Conditional was true')

language = 'Python'

if language == 'Python':
	print('Language is Python')
	language = 'Java'

elif language == 'Java':
	print('Language is Java') # Won't change because the if/ else condition is already evaluated

if language == 'Java':
	print('Language is Java')

else:
	print('Language is C++')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False

if not logged_in:
	print('Please Log In')
else:
	print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]			
print(a == b)
print(a is b)
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
print(a is b)

condition = False

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')	

condition = None

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')	

condition = -1 #only 0 is false, rest all are true

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')			

condition = []  #all empty strings, list, dictionary, tupple will evaluate to false

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')		

	
