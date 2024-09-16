immutable_var = 1, 2, 3, 'apple', 'potato', False
print(immutable_var)

mutable_list = [1, 2, 3, 'apple', 'potato', False]
print(mutable_list)
mutable_list.append('tomato')
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)
mutable_list[0] = 2
print(mutable_list)
