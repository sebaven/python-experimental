
class Parent:
    def __init__(self, name, eye_color):
        print("Parent class constructor called")
        self.last_name = name
        self.eye_collor = eye_color
    
    def show_info(self):
        """parent show_info function"""
        print("name:" + self.last_name)
        print("eye color:" + self.eye_collor)
        
        
class Child(Parent):
    def __init__(self, name, eye_color, number_of_toys):
        print("Child class constructor called")
        Parent.__init__(self, name, eye_color)
        self.number_of_toys = number_of_toys
    

    def show_info(self):
        """child show_info function"""
        Parent.show_info(self)
        print("number of toy:" + str(self.number_of_toys))

print("---------------------------")        
john_doe = Parent("Doe", "blue")
john_doe.show_info()
print(Parent.show_info.__doc__)
print("---------------------------")
emma_doe = Child("Doe", "blue", 10)
emma_doe.show_info()
print(Child.show_info.__doc__)
print("---------------------------")
    
    
