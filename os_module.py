import os
from datetime import datetime

# print(dir(os))
print(os.getcwd())

os.chdir('/Users/mohil/OneDrive/Desktop/') #used to change directory

os.mkdir('OS-Demo-2')
os.makedirs('OS-Demo-3/Sub-Dir-1')

os.rmdir('OS-Demo-2')
os.removedirs('OS-Demo-3/Sub-Dir-1')

# os.rename('hc.png', 'hb.png')

print(os.stat('aa.pdf'))
print(os.stat('aa.pdf').st_size)

mod_time = (os.stat('aa.pdf').st_mtime)
print(datetime.fromtimestamp(mod_time))

print(os.getcwd())

# print(os.listdir())

# for dirpaths, dirnames, filenames in os.walk(os.getcwd()):
# 	print('Current Path:', dirpaths)
# 	print('Directories:', dirnames)
# 	print('Files:', filenames)
# 	print()

print(os.environ.get('PYTHONPATH'))

# file_path = os.environ.get('PYTHONPATH') + 'test.txt'
# print(file_path) # not a good way, can skip some slashes

file_path = os.path.join(os.environ.get('PYTHONPATH'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/text.txt')) #gives you text.txt (Can be a mde up path)
print(os.path.dirname('/tmp/text.txt'))
print(os.path.split('/tmp/text.txt'))
print(os.path.exists('/tmp/text.txt'))
print(os.path.isdir('/tmp/text.txt'))
print(os.path.isfile('/tmp/text.txt'))
print(os.path.splitext('/tmp/text.txt')) #to get extension
print(dir(os.path))
