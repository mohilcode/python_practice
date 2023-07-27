
def hello_func():
	pass #used to avoid any errors

hello_func()
print(hello_func)
print(hello_func())

def hello_func():
	print('Hello Function!')
	return 5

hello_func()
print(hello_func)
print(hello_func()) #prints the return value

def hello_func():
	return 'Hello Function'

hello_func() #won't print anything
print(hello_func)
print(hello_func())	
print(hello_func().upper())

def hello_func(greeting):
	return '{} Function. '.format(greeting)

print(hello_func('Yo! Whats up'))

def hello_func(greeting):
	return f'{greeting} Function. '

print(hello_func('Yo! Whats up'))

def hello_func(greeting, name = 'You'):
	return '{}, {} Function. '.format(greeting, name)

print(hello_func('Yo! Whats up', 'John'))

def hello_func(greeting, name = 'You'):
	return f'{greeting}, {name} Function. '

print(hello_func('Yo! Whats up')) #uses default value
print(hello_func('Yo! Whats up', 'John'))
