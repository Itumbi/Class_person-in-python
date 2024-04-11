class person:
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

        #defining attributes 
    def introduce (self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}. ")

#creating terms for my class person
person1 = person("Juma",18,"male")
person2 = person("Alice",20,"female")
person3 = person("kiximganye",23,"male")
person4 = person("Benedicta",7,"female")

#Calling introduce to display class code
person1.introduce()
person2.introduce()
person3.introduce()
person4.introduce()
