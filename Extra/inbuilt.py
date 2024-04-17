"""
Write the useful inbuilt functions.
"""

# map function is a generator.
"""
map function is a generator function which takes function and iterable as an argument and returns the iterator object therefore when we apply next() function on the iterator object it triggers the __next__() magic method and return the next value of function.
"""

iterable = [1,2,3,4,5]

def square(x):
    return x*x

map_obj = map(square,iterable)

print(map_obj)

print(next(map_obj))  # 1

print(list(map_obj))

"""
<map object at 0x00000244AD0E27D0>
1
[4, 9, 16, 25]

"""


# filter() 

iterable = ["bob","job","mob"]

def findBOB(x:str)->int:
    if x=="bob":
        return True
    else:
        return False
    
filter_obj = filter(findBOB,iterable)

print(filter_obj)

print(next(filter_obj)) #bob

print(list(filter_obj))

"""
<filter object at 0x00000244AD0E2920>
bob
[]
"""

# enumerate()

iterable = ["bob","job","mob"]

enumerate_obj = enumerate(iterable)


print(enumerate_obj)

print(next(enumerate_obj)) #(0, 'bob')

print(list(enumerate_obj))

"""
<enumerate object at 0x00000244AD0633D0>
(0, 'bob')
[(1, 'job'), (2, 'mob')]
"""

# zip()

iterable1 = (1,2,3,4,5)
iterable2 = [0,9,8,7,6]

zip_obj = zip(iterable1,iterable2)

print(zip_obj)

print(next(zip_obj))

print(dict(zip_obj))

"""
<zip object at 0x00000244AD0F5640>
(1, 0)
{2: 9, 3: 8, 4: 7, 5: 6}
"""

