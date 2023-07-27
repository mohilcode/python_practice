import sys

# sys.path.append('/Users/mohil/OneDrive/Desktop')

# import my_module as mm
from my_module import find_index as fi, test
#from my_module import * #not recommeded, it imports everything

import random

import math
import datetime
import calendar
import os
import antigravity


courses = ['history', 'Math', 'Physics', 'CompSci']

print(os.getcwd())

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

# index = mm.find_index(courses, 'Math')
index = fi(courses, 'Math')
print(index)
print(test)

print(sys.path)

print(os.__file__)
