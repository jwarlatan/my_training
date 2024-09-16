first = 132
second = 13
third = 1324
if first != second and second != third and first != third:
    print(0)
elif first == second and second == third and first == third:
    print(3)
elif first != second or second != third or first == third:
    print(2)

