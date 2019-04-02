
### tuple comparision
print((10, 20) < (10, 30))
print((10, 20) < (10, 20, 0))
print((10, 15, 30) < (10, 20, 0))


### lambda
def lambda_test(num, func):
    return func(num)

def func(num): return num * num

print(lambda_test(10, func))
print(lambda_test(10, lambda num: num * num))

# assigning a lambda function to a variable is not recommended by PEP 8 style guide.
# func2 = lambda num: num * num
# print lambda_test(10, func2)


### format
print('Here is {} and {} is in {}'.format('Pohang', 'POSTECH', 'Pohang'))
print('Here is {0} and {1} is in {0}'.format('Pohang', 'POSTECH'))
print('Here is {city} and {univ} is in {city}'.format(city='Pohang', univ='POSTECH'))


### defaultdict
from collections import defaultdict
import traceback

d1 = dict()
d2 = defaultdict(lambda: 100)
d3 = defaultdict(int)

print(d1, d2)

try:
    print("d1['a'] --> {}".format(d1['a']))
except KeyError as e:
    print("The dictionary can't get an item with key {}".format(e))
    # traceback.print_exc()

print("d2['a'] --> {}".format(d2['a']))
print("d3['a'] --> {}".format(d3['a']))


### list comprehension
print([x**3 for x in range(10)])
print([x**3 for x in range(10) if x % 2 == 0])
print([(x, y) for x in range(10) for y in range(10) if x + y == 10])

### generator
gen = (x**3 for x in range(10) if x % 2 == 0)
print(gen)
print(list(gen))
print(list(gen))

gen = (x**3 for x in range(10) if x % 2 == 0)
while True:
    try:
        print(next(gen), end=' ')
    except StopIteration:
        break

gen = (x**3 for x in range(10) if x % 2 == 0)
for item in gen:
    print(item, end=' ')

print(tuple(x**3 % 100 for x in range(10)))
print(max(x**3 % 100 for x in range(10)))

# cf. there is another type generator, which is defined by 'yield' operation

def squre_generator(n):
    for x in range(n):
        yield x ** 2

print(tuple(squre_generator(10)))


### str.split
text = '''aa bb  cc    dd
ee ff'''
print(text)
print(text.split())              # split into strings seperated by space, tab, newline, etc

text = 'aa/bb/cc/dd/ee/ff'
print(text)
print(text.split('/'))

text = 'aa/bb/cc//dd/ee/ff'
print(text)
print(text.split('//'))


### abs
# abs means absolute values
print(abs(-10))
print(abs(10))
print(abs(100) < abs(-200))
