
# courses = ['History', 'math', 'physics', 'comp sci']
# courses_2 = courses

# print(courses)
# print(courses_2)

# courses[0] = 'Art'

# print(courses)
# print(courses_2)

#We made change just to the list 1 but list 2 also got affected (Problem with lists)

tuple_1 = ('History', 'math', 'physics', 'comp sci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art', you cant modify

set_1 = {'History', 'math', 'physics', 'comp sci'}
set_2 = {'History', 'math', 'Art', 'Design'} 

print(set_1) #Dont care about the order, also throws away the duplicates

print('math' in set_1) #Can do in tuples and lists as well but optimised for sets

print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))

#Empty List
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} #Not correct
empty_set = set()
