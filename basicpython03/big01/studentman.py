# quản lý học sinh
import re
import datetime
from utils import printHeader, clear_screen, print_menu
from dbprovider import writeStudents, writeStudent, readStudents, checkExistStudent,getStudentByCode


def studentMainScreen():
    clear_screen()
    printHeader("Quản Lý Học Viên")

    funcs = [
        '1. Thêm',
        '2. Sửa',
        '3. Xóa',
        '4. Tìm kiếm',
        '0. Trở về'
    ]
    print_menu(funcs)

    cmd = ''  # mã lệnh người dùng chọn
    while cmd not in ['0', '1', '2', '3', '4']:
        cmd = input("Chức năng: ")

    if cmd == "1":
        # chuyển sang màn hình thêm học viên
        addStudentScreen()
        # Quay lại màn hình MENU QLHV(gọi chính nó)
        studentMainScreen()
    if cmd == "2":
        editStudentScreen()
        studentMainScreen()
    if cmd == "3":
        deleteStudentScreen()
        studentMainScreen()
        pass
    if cmd == "4":
        searchStudentScreen()
        studentMainScreen()
    if cmd == "0":
        # trở về màn hình chính
        pass


def addStudentScreen():
    clear_screen()
    printHeader("Thêm Học Viên")

    # nhập dữ liệu từ bàn phím
    while True:
        code = input("Mã Học Viên:")
        if len(code) != 6:
            print("Mã học viên là chuỗi gồm 6 kí tự.")
            continue

        isExitst = checkExistStudent(code)
        if isExitst == True:
            print("Mã HV đã được sử dụng")
            continue

        if code[0:2] != 'PY':
            print("Hai kí tự đầu tiên phải là 'PY....'")
            continue
        break

    while True:
        fullName = input("Full Name:")
        if len(fullName) == 0:
            print("Bạn cần nhập vào tên của mình.")
            continue
        break

    while True:
        birthDay = input("Birth Day: ")
        if len(birthDay) == 0:
            print("Bạn cần nhập ngày tháng năm sinh của mình.")
            continue
        try:
            datetime.datetime.strptime(birthDay, '%d/%m/%Y')
        except ValueError:
            print("Cần nhập đúng định dạng 'dd/mm/yyyyy'")
            continue
        break

    while True:
        sex = input("Sex: ")
        if len(sex) == 0:
            print("Bạn cần nhập ngày giới tính của mình.")
            continue
        if sex not in ['0', '1']:
            print("Nhập đúng giới tính (0-nữ|1-nam).")
            continue
        break

    address = input("Address: ")

    while True:
        phone = input("Phone: ")
        if phone.isdigit() == False or len(phone) != 10:
            print("Số điện thoại chỉ được nhập số và có 10 kí tự.")
            continue
        break

    while True:
        email = input("Email: ")
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            break
        else:
            print("Bạn cần nhập đúng địa chỉ email")
            continue
        break

    # đổ dữ liệu vào túi dict để gửi xuống hàm writestudent trong dbprovider
    st = {
        'Code': code,
        'FullName': fullName,
        'Birthday': birthDay,
        'Sex': sex,
        'Address': address,
        'Phone': phone,
        'Email': email
    }
    writeStudent(st)
    print("Thêm học viên có mã '{}' thành công!!".format(code))

    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        addStudentScreen()


def editStudentScreen():
    clear_screen()
    printHeader("Chỉnh Sửa Thông Tin Học Viên")

    while True:
        code = input("Mã Học Viên Cần Sửa:")
        if len(code) != 6:
            print("Mã học viên là chuỗi gồm 6 kí tự.")
            continue
        isExitst = checkExistStudent(code)
        if isExitst == False:
            print("Mã HV không tồn tại.")
            continue
        break

    #Lấy thông tin theo mã học viên đã nhập
    st = getStudentByCode(code)
    print('Họ tên',st['FullName'])
    fullName = st['FullName']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # fullName = input("Họ tên mới: ") #không bỏ trống
        while True:
            fullName = input("Họ tên mới:")
            if len(fullName) == 0:
                print("Bạn cần nhập vào tên của mình.")
                continue
            break


    print('Ngày sinh',st['Birthday'])
    birthDay = st['Birthday']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # birthDay = input("Ngày sinh mới: ") #không bỏ trống
        while True:
            birthDay = input("Ngày sinh mới: ")
            if len(birthDay) == 0:
                print("Bạn cần nhập ngày tháng năm sinh của mình.")
                continue
            try:
                datetime.datetime.strptime(birthDay, '%d/%m/%Y')
            except ValueError:
                print("Cần nhập đúng định dạng 'dd/mm/yyyyy'")
                continue
            break

    print('Giới tính',st['Sex'])
    sex = st['Sex']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # sex = input("Giới tính mới: ") #không bỏ trống
        while True:
            sex = input("Giới tính mới: ")
            if len(sex) == 0:
                print("Bạn cần nhập giới tính của mình.")
                continue
            if sex not in ['0', '1']:
                print("Nhập đúng giới tính (0-nữ|1-nam).")
                continue
            break

    print('Địa chỉ',st['Address'])
    address = st['Address']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        address = input("Địa chỉ mới: ")

    print('SĐT',st['Phone'])
    phone = st['Phone']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # phone = input("SĐT mới: ") #không bỏ trống
        while True:
            phone = input("SĐT m: ")
            if phone.isdigit() == False or len(phone) != 10:
                print("Số điện thoại chỉ được nhập số và có 10 kí tự.")
                continue
            break

    print('Email',st['Email'])
    email = st['Email']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # email = input("Email mới: ") #không bỏ trống
        while True:
            email = input("Email mới: ")
            regex = re.compile(
                r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if re.fullmatch(regex, email):
                break
            else:
                print("Bạn cần nhập đúng địa chỉ email")
                continue
            break

    sts = readStudents()
    for st in sts:
        if st['Code'] == code:
            st['FullName']= fullName
            st['Birthday']= birthDay
            st['Sex']= sex
            st['Address']= address
            st['Phone']= phone
            st['Email']= email

    #sửa bằng cách sửa trên list và ghi đè với mode w vào file
    writeStudents(sts)
    print(f'Chỉnh sửa học viên có mã "{code}" thành công!!!')

    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        editStudentScreen()

def deleteStudentScreen():
    clear_screen()
    printHeader("Xóa Thông Tin Học Viên")

    while True:
        code = input("Mã Học Viên Cần Xóa:")
        if len(code) != 6:
            print("Mã học viên là chuỗi gồm 6 kí tự.")
            continue
        isExitst = checkExistStudent(code)
        if isExitst == False:
            print("Mã HV không tồn tại.")
            continue
        if code[0:2] != 'PY':
            print("Hai kí tự đầu tiên phải là 'PY....'")
            continue
        break

    sts = readStudents()
    idx = None
    for i,st in enumerate(sts):
        if st['Code'] == code:
            idx = i
            break
    sts.pop(idx)
    writeStudents(sts)
    print(f'Xóa học viên có mã "{code}" thành công!!!')

    noti = input("Nhập y/Y để tiếp tục xóa: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        deleteStudentScreen()


def searchStudentScreen():
    sts = readStudents()
    # printStudents(sts)

    searchContent = input("Nội dung tìm kiếm: ")
    if searchContent == '':
        printStudents(sts)
    else:
        stsFilter = []
        for st in sts:
            #Code,fullName,email
            if st['Code'] == searchContent or searchContent.lower() in st['FullName'].lower() or searchContent.lower() in st['Email'].lower():
                stsFilter.append(st)
        print(stsFilter)

    noti = input("Nhập y/Y để tiếp tìm kiếm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        searchStudentScreen()

def printStudents(sts:list):
    clear_screen()
    printHeader("Danh Sách Học Viên")

    print('Mã HV\tHọ tên\tNgày sinh\tGiới tính\tĐịa chỉ\tSĐT\tEmail')
    for st in sts:
        print(f"{st['Code']}\t{st['FullName']}\t{st['Birthday']}\t{st['Sex']}\t{st['Address']}\t{st['Phone']}\t{st['Email']}")

