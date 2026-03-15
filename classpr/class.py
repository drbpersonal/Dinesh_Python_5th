# from Assignment1 import nested_tuple, total

'''
class attribute
instamnce attribute
methods have multiple type
i) Instance method
ii)class method
iii)static method
iV)initializer method
'''
# class person:
#  species = 'Human'
#  def __init__(self,first_name,middle_name,last_name):
#   self.first_name = first_name
#   self.middle_name = middle_name
#   self.last_name = last_name

#  def fullname(self):
#   print(f"{self.first_name} {self.middle_name} {self.last_name}")
# p1 = person('Dinesh','Raj','Bhandari')
# p2 = person('Subrat','Raj','Gyawali')
# p3 = person('Aakash','Raj','Bhatt')
# p4 = person('Bibek','Kumar','Suvedi')
# p1.fullname()
# p2.fullname()
# p3.fullname()
# p4.fullname()
# class person:
#     species ='human'
#     legs = 2
#     def __init__(self,first_name,middle_name,last_name):
#      self.name = na
    
# class Animal:
#  legs = 4
#  @classmethod
#  def print_legs(cls):
#   print('Total legs are:',cls.legs)
# cow = Animal()
# cow.print_legs()
# cow.legs = 2
# cow.print_legs()

# class Angle:
#     _PI =3.14159
    
#     def __init__(self,value):
#      self.value = value

#     @classmethod
#     def from_radians(cls,value):
#        return cls(value)
    
#     @classmethod
#     def from_degrees(cls,value):
#        radians = value *cls._PI/180
#        return cls.from_radians(radians)
    
# a1 = Angle.from_radians(3.14159)
# a2 = Angle.from_degrees(180)

# print(a1.value)
# print(a2.value)
    

class line:
    def __init__(self,length):
        self.length = length
    #add your method here

    def __add__(self,other):
        return line(self.length + other.length)
    #end of your code
l1 = line(5)
l2 = line(10)
l3 = l1 + l2
print(type(l3))
print(l3.length)
    


