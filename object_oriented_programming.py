# everything in python is an object

# class Sample():
#     pass

# x = Sample()
# # pints type as sample
# print(type(x))


# class Dog():

#     # class object attrs
#     species = "mammal"
    
#     def __init__(self,breed, name):
#         self.breed = breed
#         self.name = name



# mydog = Dog("Lab","Trixie Ann")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)


class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(999)
print(myc.area())


# Inheritance

class Animal():
    
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("eating")

    
mya = Animal()
mya.whoAmI()
mya.eat()


class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print("Dog Created")
    
    def bark(self):
        print("Woof!")

    def eat(self):
        print("dog eating")


myb = Dog()
myb.whoAmI()
myb.bark()
myb.eat()


# Special Methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation
    def __str__(self):
        return "Titie: {}, Pages: {}, Author: {}".format(self.title,self.pages,self.author)

    # length
    def __len__(self):
        return self.pages

    # delete
    def __del__(self):
        print("a book is destroyed")

b = Book("Python","jose",200)

print(b)
# calling the length
print(len(b))
del b