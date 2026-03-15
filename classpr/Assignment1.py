# Question Q001: Identity and Membership Operations
# Q001-1: check whether the number 12 is an integer or not
num = 12
print(isinstance(num, int))
'''
Output:
    True
'''

# Q001-2: divide 100 by 12 and check whether the result is float or not
result = 100 / 12
print(isinstance(result, float))
# True

# Q001-3: create lists x, y and z
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = x

# Q001-4: check whether x is identical to y
print(x is y)

# Q001-5: check whether x is identical to z
print(x is z)

'''Output:
   False
   True
'''

# Q001-6: check whether lion is in the zoo or not
zoo = ["elephant", "tiger", "zebra", "lion", "wolf"]
print("lion" in zoo)

''' Output:
    True
'''

# Q001-7: check whether horse is in the zoo or not
print("horse" in zoo)

''' Output:
    False
'''
# Q001-8: create list of first 7 prime numbers and check 9
primes = [2, 3, 5, 7, 11, 13, 17]
print(9 in primes)
''' Output:
    False
'''

# Question Q002: List Creation and Methods
# Q002-1: create an empty list
my_list = []

# Q002-2: add numbers 5 and 9 using append()
my_list.append(5)
my_list.append(9)

# Q002-3: take input from user and add to list
num = int(input("Enter a number: "))
my_list.append(num)

# Q002-4: create another list and extend my_list
more_items = [1, 2, 3]
my_list.extend(more_items)

# Q002-5: find length of the list
print(len(my_list))

# Q002-6: remove second item using pop()
removed_item = my_list.pop(1)
print(my_list)

# Q002-7: check whether popped item exists in list
print(removed_item in my_list)

# Output:
'''
Enter a number: 6
6
[5, 6, 1, 2, 3]
False
'''

# Question Q003: Wild Animals List
# Q003-1: create list of wild animals
wild = ["tiger", "lion", "deer", "bear", "zebra"]

# Q003-2: sort the list
wild.sort()

# Q003-3: reverse the list
wild.reverse()

# Q003-4: add three more animals
wild.extend(["leopard", "elephant", "rhino"])

# Q003-5: find position of leopard and remove it
pos = wild.index("leopard")
wild.pop(pos)

# Q003-6: check whether leopard is removed
print("leopard" in wild)

# Q003-7: add leopard again at index 2
wild.insert(2, "leopard")

# Q003-8: remove rhino using remove()
wild.remove("rhino")
print(wild)

'''
Output:
False
['zebra', 'tiger', 'leopard', 'lion', 'deer', 'bear', 'elephant']
'''

# Question Q004: Multi-Dimensional List
# Q004-1: create nested list
multi = [
    [12, 52, 37],
    [46, 51, 16],
    [17, 82, 39]
]

# Q004-2: access number 51
print(multi[1][1])

# Q004-3: access number 82 using negative index
print(multi[-1][-2])

# Q004-4: find length of outer list
print(len(multi))

# Q004-5: append another list
multi.append([40, 61, 10])

# Q004-6: print each list using loop
for i in multi:
    print(i)

# Q004-7: print each element using nested loop
for i in multi:
    for j in i:
        print(j)

# Q004-8: find length of each inner list
for i in multi:
    print(len(i))

# Q004-9: clear the list
multi.clear()
print(multi)

'''
Output:
51
82
3
[12, 52, 37]
[46, 51, 16]
[17, 82, 39]
[40, 61, 10]
12
52
37
46
51
16
17
82
39
40
61
10
3
3
3
3
[]
'''

# Question Q005: Tuple Operations
# Q005-1: create tuple with 5 numbers
t = (10, 20, 30, 40, 50)

# Q005-2: find length of tuple
print(len(t))

# Q005-3: access third element
print(t[2])

# Q005-4: use enumerate()
for i, v in enumerate(t):
    print(i, v)
'''
Output:
5
30
0 10
1 20
2 30
3 40
4 50
'''

# Question Q006: Nested Tuple
# Q006-1: create nested tuple
nested_tuple = ((1, 2, 3), (4, 5, 6))

# Q006-2: access element using positive index
print(nested_tuple[1][1])

# Q006-3: access element using negative index
print(nested_tuple[-1][-2])

'''
Output:
5
5
'''
# Question Q007: Tuple Unpacking
# Q007-1: create two tuples
t1 = (1, 6, 9, 4, 3)
t2 = (2, 7, 8, 3, 5)

# Q007-2: create new tuple using unpacking
t3 = (*t1, *t2)
print(t3)

'''
Output:
(1, 6, 9, 4, 3, 2, 7, 8, 3, 5)
'''

# Question Q008: Set Operations
# Q008-1: create sets
rich = {"USA", "China", "Japan", "Germany", "France", "Australia", "Italy"}
europe = {"Germany", "France", "England", "Switzerland", "Italy", "Portugal", "Sweden"}

# Q008-2: rich but not Europe
print(rich - europe)

# Q008-3: Europe but not rich
print(europe - rich)

# Q008-4: common countries
print(rich & europe)

# Q008-5: either rich or Europe but not both
print(rich ^ europe)

# Q008-6: all unique countries
print(rich | europe)

# Q008-7: check disjoint
print(rich.isdisjoint(europe))

# Q008-8: remove common countries and check again
rich.difference_update(europe)
print(rich.isdisjoint(europe))

# Q008-9: subset and superset checks
asian_rich = {"China", "Japan"}
print(asian_rich.issubset(rich))
print(rich.issuperset(asian_rich))

'''
Output:
{'Japan', 'USA', 'China', 'Australia'}
{'Sweden', 'England', 'Portugal', 'Switzerland'}
{'Italy', 'France', 'Germany'}
{'Australia', 'Sweden', 'England', 'China', 'USA', 'Japan', 'Portugal', 'Switzerland'}
{'France', 'Switzerland', 'Australia', 'Italy', 'Sweden', 'England', 'China', 'Japan', 'Germany', 'Portugal', 'USA'}
False
True
True
True
'''

# Question Q009: Dictionary Basics
# Q009-1: create dictionary
person = {"name": "Ram", "age": 25, "profession": "Teacher", "married": False}

# Q009-2: print name
print(person["name"])

# Q009-3: add age by 10
print(person["age"] + 10)

# Q009-4: access employed key using get()
print(person.get("employed"))

# Q009-5: get with default value
print(person.get("employed", False))

'''
Output:
Ram
35
None
False
'''
# Question Q010: Dictionary Operations
# Q010-1: create car dictionary
car = {"brand": "Toyota", "model": "Corolla", "price": 20000}

# Q010-2: add engine key
car["engine"] = "Petrol"

# Q010-3: update multiple keys
car.update({"color": "Red", "seats": 5})

# Q010-4: remove color key
car.pop("color")

# Q010-5: use popitem()
car.popitem()

# Q010-6: iterate keys
for k in car:
    print(k)

# Q010-7: iterate values
for v in car.values():
    print(v)

# Q010-8: iterate items
for k, v in car.items():
    print(k, v)

'''
Output:
brand
model
price
engine
Toyota
Corolla
20000
Petrol
brand Toyota
model Corolla
price 20000
engine Petrol
'''

# Question Q011: Nested Dictionary
# Q011-1: create nested dictionary
yoda = {
    "master": {
        "master": {
            "affiliations": ["house Serenno", "jedi"]
        }
    }
}

# Q011-2: print first affiliation
print(yoda["master"]["master"]["affiliations"][0])

# Q011-3: add Sith affiliation
yoda["master"]["master"]["affiliations"].append("Sith")

# Q011-4: pop master key
yoda.pop("master")

# Output: house Serenno

# Question Q012: Type Hinting
# Q012-1: integer type hint
odd: int = 7

# Q012-2: float type hint
PI: float = 3.1415

# Q012-3: string type hint with integer value
name: str = 10
print(odd, PI, name)
#Output: 7 3.1415 10

# Question Q013: Type Conversion
# Q013-1: convert float to int
print(int(3.1415))
# Output:
# 3

# Q013-2: convert strings to integers and add
print(int("20") + int("30"))
# Output:
# 50

# Q013-3: sum list of string numbers
x = ['1', '2', '3', '4', '5']
total = 0
for i in x:
    total += int(i)
print(total)
# Outout: 15

# Q013-4: odd and prime operations
odd = [1, 3, 5, 7, 9, 11, 13]
prime = [2, 3, 5, 7, 11, 13]
print(list(set(odd) - set(prime)))
# Output:[1, 9]

# Question Q014: Palindrome Program
# Q014-1: check whether input word is palindrome
while True:
    word = input("Enter word (blank to exit): ")
    if not word:
        break

    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
'''
Output:
Enter word (blank to exit): 4
Palindrome
'''