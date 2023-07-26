message = 'Hello World'
cupid = message.replace('World', 'Universe')
message1 = 'Bobby\'s World'
message2 = """Hi My name is
Mohil Garg"""
message3 = message + ', ' + cupid + '. Welcome!'
message4 = '{}, {}. Welcome!'.format(message, cupid)
message5 = f'{message}, {cupid}. Welcome!'
message6 = f'{message}, {cupid.upper()}. Welcome!'
print(message.count('Hello'))
print(message.find('World'))
print(message.find('Universe'))
print(message.lower())
print(message.upper())
print(message[4:11])
print(message1)
print(message2)
print(cupid)
print(message3)
print(message4)
print(message5)
print(message6)
print(dir(message))
print(help(str))
print(help(str.lower))
