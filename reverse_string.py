original_string = "Hello, World!"
reversed_string = original_string[::-1]
print(reversed_string)

original_string = "Hello, World!"
reversed_string = ''.join(reversed(original_string))
print(reversed_string)

original_string = "Hello, World!"
reversed_string = ''
for char in original_string:
    reversed_string = char + reversed_string
print(reversed_string)
