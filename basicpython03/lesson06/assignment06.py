# B1
class shape:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height


class shape_rec(shape):
    def area(self):
        return self.Height*self.Width


class shape_tri(shape):
    def __init__(self, hypotenuse, height):
        self.Hypotenuse = hypotenuse
        self.Height = height

    def area(self):
        return (self.Hypotenuse*self.Height)*0.5


print("Diện tích HCN là: ", shape_rec(3, 5).area())
print("Diện tích HTG là: ", shape_tri(5, 5).area())

# B2
class Mother:
    def display(self):
        print("mother!")


class child(Mother):
    def display(self):
        print("Child")


lopCon = child()
lopCon.display()

# B3
class Animal:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
class c_Zebra(Animal):
    def f_Zebra(self):
        print(f"The Zebra name {self.Name} is {self.Age} years old.")
class c_Dolphin(Animal):
    def f_Dolphin(self):
        print(f"The Dolphin name {self.Name} is {self.Age} years old.")


Zebra1 = c_Zebra('Zebra',2).f_Zebra()
Dolphin1 = c_Dolphin("Dolphin1", 10).f_Dolphin()
