# quản lý môn học
from utils import printHeader, clear_screen, print_menu
from dbprovider import writeSubject, writeSubjects, readSubjects, checkExistSubject,getSubjectByCode,checkExistSubjectName


def subjectMainScreen():
    clear_screen()
    printHeader("Quản Lý Môn Học")

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
        # chuyển sang màn hình thêm môn học
        addSubjectScreen()
        # Quay lại màn hình MENU QLHV(gọi chính nó)
        subjectMainScreen()
    if cmd == "2":
        editSubjectScreen()
        subjectMainScreen()
    if cmd == "3":
        deleteSubjectScreen()
        subjectMainScreen()
    if cmd == "4":
        searchSubjectScreen()
        subjectMainScreen()
    if cmd == "0":
        # trở về màn hình chính
        pass


def addSubjectScreen():
    clear_screen()
    printHeader("Thêm Môn Học")
    while True:
        code = input("Mã Môn Học:")
        if len(code) != 6:
            print("Mã môn học là chuỗi gồm 6 kí tự.")
            continue

        if code[0:2] != 'MH':
            print("Hai kí tự đầu tiên phải là 'MH....'")
            continue

        isExitstcode = checkExistSubject(code)
        if isExitstcode == True:
            print("Mã Môn Học đã được sử dụng")
            continue
        break

    while True:
        name = input("Nhập tên môn học: ")
        if len(name) == 0:
            print("Bạn cần nhập vào tên Môn Học mình.")
            continue
        isExistname = checkExistSubjectName(name)
        if isExistname == True:
            print("Tên Môn Học đã được sử dụng")
            continue
        break

    sb = {
        'Code': code,
        'Name': name
    }

    writeSubject(sb)
    print("Thêm môn học có mã '{}' thành công!!".format(code))

    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        addSubjectScreen()


def editSubjectScreen():
    clear_screen()
    printHeader("Chỉnh Sửa Thông Tin Môn Học")

    while True:
        code = input("Mã Môn Học Cần Sửa:")
        if len(code) != 6:
            print("Mã Môn Học là chuỗi gồm 6 kí tự.")
            continue
        isExitst = checkExistSubject(code)
        if isExitst == False:
            print("Mã MH tồn tại.")
            continue
        break

    #Lấy thông tin theo mã môn học đã nhập
    sb = getSubjectByCode(code)

    print('Tên Môn Học',sb['Name'])
    name = sb['Name']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        while True:
            name = input("Nhập tên môn học mới: ")
            if len(name) == 0:
                print("Bạn cần nhập vào tên Môn Học mình.")
                continue
            break
    
    sbs = readSubjects()
    for sb in sbs:
        if sb['Code'] == code:
            sb['Code']= code
            sb['Name']= name
            break
    writeSubjects(sbs)
    print('Chỉnh sửa môn học thành công!!!')
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        editSubjectScreen()

def deleteSubjectScreen():
    clear_screen()
    printHeader("Xóa Thông Tin Môn Học")

    while True:
        code = input("Mã Môn Học cần xóa:")
        if len(code) != 6:
            print("Mã môn học là chuỗi gồm 6 kí tự.")
            continue

        if code[0:2] != 'MH':
            print("Hai kí tự đầu tiên phải là 'MH....'")
            continue

        isExitst = checkExistSubject(code)
        if isExitst == False:
            print("Mã Môn Học không tồn tại")
            continue
        break

    sbs = readSubjects()
    idx = None
    for i,sb in enumerate(sbs):
        if sb['Code'] == code:
            idx = i
            break

    sbs.pop(idx)
    writeSubjects(sbs)
    print(f'Xóa học viên có mã "{code}" thành công!!!')

    noti = input("Nhập y/Y để tiếp tục xóa: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        deleteSubjectScreen()



def searchSubjectScreen():
    sbs = readSubjects()
    # printSubjects(sbs)

    searchContent = input("Nội dung tìm kiếm: ")
    if searchContent == '':
        printSubjects(sbs)
    else:
        stsFilter = []
        for sb in sbs:
            #Code,Name
            if sb['Code'] == searchContent or searchContent.lower() in sb['Name'].lower() :
                stsFilter.append(sb)
        printSubjects(stsFilter)

    noti = input("Nhập y/Y để tiếp tìm kiếm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        searchSubjectScreen()

def printSubjects(sbs:list):
    clear_screen()
    printHeader("Danh Sách Môn Học")

    print('Mã MH\tTên MH')
    for sb in sbs:
        print(f"{sb['Code']}\t{sb['Name']}")

