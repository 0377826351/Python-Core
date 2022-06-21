import datetime
num = int(input("Số xe cần nhập: "))
listCars = []
for i in range(num):
    maXE = input("Nhập mã xe: ")
    nhanHieu = input("Nhập nhãn hiệu: ")
    dongXe = input("Nhập dòng xe: ")
    mauSac = int(input("Nhập màu sắc (1-đen, 2-trắng, 3-đỏ, 4-xanh nước biển): "))
    namSX = int(input("Nhập năm sản xuất: "))
    xe = {'maXE':maXE,"nhanHieu":nhanHieu,'dongXe':dongXe,'mauSac':mauSac,'namSX':namSX}
    listCars.append(xe)

yearNow = datetime.datetime.now()
carFilter = list(filter(lambda x:x['mauSac'] == 1 and x['namSX']>=2015 and x['namSX'] <= yearNow.year, listCars))
print("Danh sách xe có màu đen và sản xuất từ năm 2015 đến nay: ")
print(carFilter)
    
#B2
print("Danh sách xe ban đầu: ")
for i in listCars:
    print(i)
def changeColor(car:dict):
    if car['mauSac'] == 1:
        car['mauSac'] = "Đen"
    return car
newCar = map(changeColor,listCars)
print("Danh sách xe sau khi đã đổi màu sắc: ")
for i in newCar:
    print(i)