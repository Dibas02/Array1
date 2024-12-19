import array as arr

a = arr.array('i', [1, 3, 4, 3, 7, 3750])

print(a)


print("the number of values in the array is", len(a))

print("the frequency of 3 in the array is", a.count(3))
a.reverse()
print(a)

a.append(100)

print(a)

a.insert(5, 21)

print(a)

a.pop(1)
print(a)

a.remove(21)
print(a)

