my_dict = {'one' : 123, 'two' : 456, 'three' : 789}
print(my_dict)
print(my_dict.get('one'))
print(my_dict.get('four'))
my_dict.update({'four' : 153, 'five' : 759})
print(my_dict)
a = my_dict.pop('one')
print(a)
print(my_dict)

my_set  = {1, 2, 'one', 5, 1, 5}
print(my_set)
my_set.update({'six', 6})
print(my_set)
print(my_set.discard(1))
print(my_set)
print(type(my_dict))






