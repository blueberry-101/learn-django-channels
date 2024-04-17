"""
A generator in Python is a function that returns an iterator. This means that it can be used to generate a sequence of values, one at a time. Generators are often used to create infinite sequences, such as the Fibonacci sequence.
To create a generator, you use the yield keyword instead of the return keyword. When a generator yields a value, it pauses its execution and returns the value. The next time the generator is called, it resumes execution where it left off.
Here is an example of a generator function:
"""

# a list tuple are the iterables and the generator is a function that returns an iterator which has a special dunder method __next__() jiski help se hum
# bina for loop ke iterator par iteration kar sakte hain. though for loop se bhi kar sakte hain.

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

numbers = fibonacci()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


# Difference between iterators and iterables.



listo = [1,2,3,4,5,5] # list object is not iterator its iterable
listo = iter(listo) #convert into iterator
print(next(listo))
print(next(listo))
print(next(listo))
print(next(listo))

# a list tuple are the iterables and the generator is a function that returns an iterator which has a magic method __next__() jiski help se hum
# bina for loop ke iterator par iteration kar sakte hain. though for loop se bhi kar sakte hain.

"""
A list object is not an iterator because it does not have a __next__() method. Thus calling the next() function (which would call the __next__() method on an object if it has one) on a list would result in a TypeError, since our list object is not an iterator and thus does not have a __next__() method.
"""

