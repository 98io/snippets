# python types
i = 5
# <class 'int'>
print(type(i))

# cast 
# 5
print(int(5.5))
# 1
print(int(True))

# tuple: immutable
x = (0, 1, 2) 
# 0
print(x[0])
# 2
print(x[-1])

# List: mutable
l = [10, 9, 15]
l.extend([11, 20])
# [10, 9, 15, 11, 20]
print(l)
