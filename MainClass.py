from models import Mammals
from models import Parrot
from models import Penguin
from models import Animal
from models import Point

# OOPS in python started
'''
def test_fly(bird):
    bird.fly()


mammal = Mammals()
mammal.printMembers();

parrot = Parrot();
penguin = Penguin();

test_fly(parrot)
test_fly(penguin)

print(isinstance(mammal, Animal))
print(issubclass(Mammals, Animal))
print(issubclass(bool, int))

p1 = Point(10, 20)
p2 = Point(30, 40)

print(p1)

print(p1+p2)

'''

# OOPS in python end

# python basics started

# Numbers
a = 5;
print(a, "is of type", type(a))

a = 2.45
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex  number ? ", isinstance(1+2j, complex))


a = [1, 2.2, 'python']
print(a)

# List
# Array starts with 0 index
a = [5, 10, 15, 20, 25, 30, 35, 40]
print("List length is ", a.__len__())
print("a[2] = ", a[2])
# Excludes right side of colon, means starts with 0 and pick 3 values
print("a[0:3] = ", a[0:3])
# Starts with index 5 till end
print("a[5:] = ", a[5:])

# Tuple
t = (5, 'program', 1+3j)

print("t[1] = ", t[1])
print("t[0:3] = ", t[0:3])
# Generate error, not able to assign it as tuples are immutable
# t[0] = 10;

# Strings
s = "Hello world!"
print("s[4] = ", s[4])
# Excludes right side of colon
print("s[6:11] = ", s[6:11])

# Generate error, strings are immutable 
#s[5] = 'd'

# Set, slicing [] does not work in set
a = {1, 2, 3, 3, 4, 5}
b = {10, 8, 3}
c = a.union(b)
d = a.intersection(b)
print(a)
print(c)
print(d)

# Dictionary

d = {1:'value', 'key':2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])
#Generates error, No Key error
#print("d[2] = ", d[2])

# Conversion between two numbers
print(float(5))
print(int(5.97))
print(float('5.78'))
print(str(5))
print(int('5'))
# Conversion error
# print(int('5p'))

print(set([1, 2, 3, 3, 4]))
print(tuple({1, 2, 3, 4}))
print(list('hello'))
print(dict([[1, 2], [3, 4]]))
print(dict([(1, 2), (3, 4)]))

# Output and Input
x = 5
y = 10
print('The vale of x is {} and y is {}'.format(x,y))
print('I love {0} and {1}'.format('bread', 'butter'))
print('I love {1} and {0}'.format('bread', 'butter'))
print('Hello {name},  {greeting}'.format(greeting = 'Good Morning', name = 'John'))

num = input('Enter a number : ')
print("Entered Number is : ", int(num))
# Error
#print("Expression evaluation : ", int('2+3'))
print("Expression evaluation : ", eval('2+3'))



# python basics end

