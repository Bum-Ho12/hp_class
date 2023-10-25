class cars:
    # constructor
    def __init__(self,type ,color,model):
        self.type=type
        self.color=color
        self.model=model
    # method
    def show(self):
        print(f"I love {self.model} {self.type} vehicles of {self.color} color")
        # creating object
my_obj = cars("saloon","white","Toyota")
my_obj.show()

class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age
    def display(self):
        print("Name: %s \ncourse: %s\n gender: %s\nage: %d" % (self.name,self.course,self.gender,self.age))
student = students("Bumho","Comp Tech","male",23)
student.display()