#  tuple_1=()
# tuple_2=(1,2,3)
# print(type(tuple_2))
# odd = (1, 3, 5, 7, 9)
# even = (0, 2, 4, 6, 8)
# even = list(even)
# even[-1]=10
# even = tuple(even)
# print(even)
# person = {
#     'name': 'Dinesh',
#     'age': 23,
#    'married': False,
# }
# print(person['age'])
# print(person['married'])
# income = {
#     'salary': 50000,
#     'bonus': 5000,
#     'rental_income': 20000,
# }
# other_sources = {
#     'uber':600,
#     'freelancing': 2000,
#     'salary': 70000
# }
# income.update(other_sources)
# total_income = income['salary'] + income['bonus'] + income['rental_income']
# print(income.get('bonus'))
# print(total_income)
# income.pop('rental_income')
# value = income.pop('bonus')
# print(value)
# print(income)
# (key,value) = ('name','Dinesh')
# print(key)

# person = {
#     'name': 'Ram',
#     'age': 25,
#     'roll_no': 101,
#     'married': False,
# }
# print(person.keys())
# print(person.values())
# print(person.items())
# for key, value in person.items():
#     print(f'Key: {key}, Value: {value}')

# numbers = {1, 2, 3, 4, 5}
# animals = {'cat', 'dog', 'elephant'}
# random_list = {1, 'hello', 3.14, True, None}
# numbers = {1,2,3,4,5,6,4,3,2,1}
# print(numbers)

# even = {0, 2, 4, 6, 8}
# even.discard(34)
# print(even)
# even.remove(34)
# print(even)
# odd = {1, 3, 5, 7, 9}
# all_numbers = even.union(odd)

# nested_list =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# nested_tuple= (
#     ('a','apple'),
#     ('b','banana'),
#     ('c','cherry'),
# )
# students =[
#     {
#         'name': 'Dinesh',
#         'age': 23,
#         'marks': [85, 90, 78],
#     },
#     {
#         'name': 'Anita',
#         'age': 22,
#         'marks': [88, 92, 80],
#     },
# ]

#Create a nested dictionary named yoda with following properties
#age:910
#species:yodas
#gender:male
#affiliations:['jedi','Galactic Republic']
#master:
#name:Qui-Gon Jinn
#age: 48
#affiliations:['jedi order','Hellost clan']
#master
#name: Dooku
#age:83
#affiliations:['house Serenno','jedi']
# yoda= {
#         'age':910,
#         'species':'yodas',
#         'gender':'male',
#         'affiliations':['jedi','Galactic Republic'],        
     
#         'master':{
#             'name':'Qui-Gon Jinn',
#             'age':48,
#             'affiliations':['jedi order','Hellost clan'],
#             'master':{
#                 'name':'Dooku',
#                 'age':83,
#                 'affiliations':['house Serenno','jedi'],
#             }
            

#         }
#     }     
# print(yoda['master']) 
# print(yoda['master']['master']['affiliations'])

# num=24
# if num % 3 == 0:
#     print("Divisible by only 3")
# elif num % 2 == 0:
#     print("Divisible by only 2")
# elif num % 2 == 0 and num % 3 == 0:
#     print("Divisible by both 2 and 3")

# number = int(input("Enter a number: "))
# match number:
#     case 1:
#         print("You entered one")
#     case 2: 
#         print("The lucky number")
#     case 3:
#         print("You entered three")

# x = 10
# if x < 7:
#     size =' small'

# elif x >= 7 and x < 1:
#     size = 'medium'
# else:
#     size = 'large'

# print(size)
# size =' small' if x < 7 else 'medium' if(7 <=x < 10)else'large'
# print(size)
# convert to match case for above code


#"LOOP"2082-10-11
  #print the value from 1 upto 10
# x= 1
# while x<=10:
#     print('The current value of x is:',x)
#     x+=1
#     print('The loop is completed')

# name_list =[]
# name=''
# while name.lower() !='exit':
#     name=input('Enter the name:')
#     name_list.append(name)
#     print(name_list[:-1])

# x =0
# while x < 5:
#     print(f'The current value of x is: {x}')
#     x += 1

#Nested While Loop
# num = 4
# while num <= 6:
#     mul = 1
#     while mul <= 10:
#         print(f'{num:>2} x {mul:>2} = {(num * mul):>2}', end='\t')
#         mul += 1
#         print()
#         num += 1 

# pattern generation
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()