#OOP bao đóng,kế thừa(đơn,đa),đa hình,trừu tượng

class dog:
    # hàm khởi tạo khi tạo mới 1 object
    # chạy đầu tiên khi đối tượng được khởi tạo
    # không xử lý logic phức tạp ở đây,mục đích để setup/chuẩn bị/khởi tạo dữ liệu
    def __init__(self, breed: str, size: str, color: str, age: int):
        # Các thuộc tính (attributes/fields)
        self.Breed = breed
        self.Size = size
        self.Color = color
        self.Age = age

    #Các phương thức (methods)
    def Eat(self):
        print('Eat!')

    def Run(self):
        print('Run!')

    def Sleep(self):
        print('Sleep')

    def __Speak(self):
        print('Speak')

bullDog = dog(breed = 'Bull Dog',size = 'Small',color = 'black',age = 2)
# print(bullDog)
# print(bullDog.Breed)
# print(bullDog.Size)
# print(bullDog.Color)
# print(bullDog.Age)

# bullDog.Eat()
# bullDog.Run()
# bullDog.Sleep()
#bullDog.__Speak() #không truy cập được


#Đây là đơn kế thừa
#Đây là một lớp cha/lớp cơ sở/base class/super class
class Animal:
    def __init__(self,breed,color,age):
        self.Breed = breed
        self.Color = color
        self.Age = age

    def Speak(self):
        print("Speaking...")

#Lớp con/lớp dẫn xuất/sub_class
# Tạo ra 1 lớp dog kế thừa từ lớp Animal  
class Dog(Animal):
    def __init__(self,breed,color,age,birth,origin):
        #call hàm khởi tạo của lớp cha
        super().__init__(breed,color,age)

        #khởi tạo thuộc tính của riêng lớp Dog 
        self.Birth = birth
        self.Origin = origin

    def Speak(self):
        # CAll hàm speak từ lớp cha
        super().Speak()
        print('Gau Gau...')

class Cow(Animal):
    def __init__(self,breed,color,age,hornSize):
        #call hàm khởi tạo của lớp cha
        super().__init__(breed,color,age)

        #khởi tạo thuộc tính của riêng lớp Dog 
        self.HornSize = hornSize

    def Speak(self):
        # CAll hàm speak từ lớp cha
        super().Speak()
        print('Bo bo...')


# dog1 = Dog('Lai','Đen',2,'1/1/2020','My')
# print(dog1.Breed)
# print(dog1.Color)
# print(dog1.Age)
# print(dog1.Birth)
# print(dog1.Origin)
# dog1.Speak()

# bo = Cow('Lai','Trang','3','10')
# print(bo.Breed)
# print(bo.Color)
# print(bo.Age)
# print(bo.HornSize)
# bo.Speak()

#Đa kế thừa
class A:
    def funcA(self):
        print("FunA")

class B:
    def funcB(self):
        print("FunB")

class C(A, B):
    def funcC(self):
        print("FunC")

c= C()
c.funcA()
c.funcB()
c.funcC()

# Phương thức isinstance () được sử dụng để kiểm tra mối quan hệ giữa các đối tượng và các lớp. 
# Nó trả về true nếu tham số đầu tiên, tức là obj là thể hiện của tham số thứ hai, tức là lớp.
# print(isinstance(3,int)) #true
# print(isinstance((3,),tuple)) #
# print(isinstance(3,int))

# Phương thức issubclass(sub, sup) được sử dụng để kiểm tra mối quan hệ giữa các lớp được chỉ định. 
# Nó trả về true nếu lớp thứ nhất là lớp con của lớp thứ hai và ngược lại là false  .
print(issubclass(C,A))

