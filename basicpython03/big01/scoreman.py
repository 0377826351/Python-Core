# quản lý điểm
from utils import printHeader, clear_screen, print_menu
from dbprovider import writeScore, writeScores, readScores,checkExistScore,checkExistSubject,checkExistStudent,getScoreByCode,readStudents,readSubjects,phanLoai
import csv

def scoreMainScreen():
    clear_screen()
    printHeader("Quản Lý Điểm Thi")

    funcs = [
        '1. Thêm',
        '2. Sửa',
        '3. Xóa',
        '4. Tìm kiếm',
        '5. Thống kê',
        '6. Xuất ra file csv',
        '0. Trở về'
    ]
    print_menu(funcs)

    cmd = ''  # mã lệnh người dùng chọn
    while cmd not in ['0', '1', '2', '3', '4', '5','6']:
        cmd = input("Chức năng: ")

    if cmd == "1":
        # chuyển sang màn hình thêm điểm thi
        addScoreSubject()
        # Quay lại màn hình MENU QLHV(gọi chính nó)
        scoreMainScreen()
    if cmd == "2":
        editScoreScreen()
        scoreMainScreen()
    if cmd == "3":
        deleteScoreScreen()
        scoreMainScreen()
    if cmd == "4":
        searchScoreScreen()
        scoreMainScreen()
    if cmd == "5":
        statisticalScore()
        scoreMainScreen()
    if cmd == '6':
        xuatFile()
        scoreMainScreen()
    if cmd == "0":
        # trở về màn hình chính
        pass

def addScoreSubject():
    clear_screen()
    printHeader("Thêm Điểm Thi")
    while True:
        studentCode = None
        subjectCode = None
        while True:
            studentCode = input("Nhập mã học viên: ")
            if len(studentCode) != 6:
                print("Mã học viên là chuỗi gồm 6 kí tự.")
                continue

            if studentCode[0:2] != 'PY':
                print("Hai kí tự đầu tiên phải là 'PY....'")
                continue

            isExitst = checkExistStudent(studentCode)
            if isExitst == False:
                print("Mã HV không tồn tại")
                continue
            break

        while True:
            subjectCode = input("Nhập mã môn học: ")
            if len(subjectCode) != 6:
                print("Mã môn học là chuỗi gồm 6 kí tự.")
                continue

            if subjectCode[0:2] != 'MH':
                print("Hai kí tự đầu tiên phải là 'MH....'")
                continue

            isExitst = checkExistSubject(subjectCode)
            if isExitst == False:
                print("Mã Môn Học không tồn tại")
                continue
            break

        isExitstScore = checkExistScore(studentCode,subjectCode)
        if isExitstScore == True:
            print("Điểm của môn học đã có.")
            continue
        break
    
    while True:
        processPoint = input("Nhập điểm quá trình: ")
        if processPoint == '':
            print("Không được để trống điểm.")
            continue
        # TODO check la so
        if float(processPoint) < 0 or float(processPoint) >10:
            print("Nhập lại điểm (0-10).")
            continue
        break
    
    while True:
        endPoint = float(input("Nhap điểm kết thúc: "))
        if endPoint < 0 or endPoint > 10:
            print("Nhập lại điểm (0-10).")
            continue
        if endPoint == None:
            print("Không được để trống điểm.")
            continue
        break

    sc = {
        'Student_Code': studentCode,
        'Subject_Code': subjectCode,
        'processPoint': processPoint,
        'endPoint': endPoint
    }

    writeScore(sc)
    print("Thêm điểm thành công!!")

    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        addScoreSubject()

def editScoreScreen():
    clear_screen()
    printHeader("Chỉnh Sửa Thông Tin Điểm")

    while True:
        studentCode = input("Mã Học Viên cần sửa:")
        if len(studentCode) != 6:
            print("Mã học viên là chuỗi gồm 6 kí tự.")
            continue
        if studentCode[0:2] != 'PY':
            print("Hai kí tự đầu tiên phải là 'PY....'")
            continue
        isExitst = checkExistStudent(studentCode)
        if isExitst == False:
            print("Mã HV không tồn tại.")
            continue
        break

    while True:
        subjectCode = input("Mã Môn Học cần sửa: ")
        if len(subjectCode) != 6:
            print("Mã Môn Học là chuỗi gồm 6 kí tự.")
            continue
        if subjectCode[0:2] != 'MH':
            print("Hai kí tự đầu tiên phải là 'MH....'")
            continue
        isExitst = checkExistSubject(subjectCode)
        if isExitst == False:
            print("Mã MH không tồn tại.")
            continue
        break

    sc = getScoreByCode(studentCode,subjectCode)

    print('Điểm quá trình:',sc['processPoint'])
    processPoint = sc['processPoint']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        while True:
            processPoint = input("Nhập điểm quá trình mới: ")
            break

    print('Điểm kết thúc:',sc['endPoint'])
    endPoint = sc['endPoint']
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        while True:
            endPoint = input("Nhập điểm kết thúc mới: ")
            break

    scs = readScores()
    for sc in scs:
        if sc['Student_Code'] == studentCode and sc['Subject_Code'] == subjectCode:
            sc['processPoint']= processPoint
            sc['endPoint']= endPoint
            break
    writeScores(scs)
    print('Chỉnh sửa điểm thành công!!!')
    noti = input("Nhập y/Y để tiếp tục thêm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        editScoreScreen()

def deleteScoreScreen():
    clear_screen()
    printHeader("Xóa Thông Tin Điểm")

    while True:
        studentCode = input("Mã Học Viên cần sửa:")
        if len(studentCode) != 6:
            print("Mã học viên là chuỗi gồm 6 kí tự.")
            continue
        if studentCode[0:2] != 'PY':
            print("Hai kí tự đầu tiên phải là 'PY....'")
            continue
        isExitst = checkExistStudent(studentCode)
        if isExitst == False:
            print("Mã HV không tồn tại.")
            continue
        break

    while True:
        subjectCode = input("Mã Môn Học cần sửa: ")
        if len(subjectCode) != 6:
            print("Mã Môn Học là chuỗi gồm 6 kí tự.")
            continue
        if subjectCode[0:2] != 'MH':
            print("Hai kí tự đầu tiên phải là 'MH....'")
            continue
        break
        isExitst = checkExistSubject(subjectCode)
        if isExitst == False:
            print("Mã MH không tồn tại.")
            continue

    scs = readScores()
    idx = None
    for i,sc in enumerate(scs):
        if sc['Student_Code'] == studentCode and sc['Subject_Code'] == subjectCode:
            idx = i
            break
    
    scs.pop(idx)
    writeScores(scs)
    print(f'Xóa điểm thành công!!!')

    noti = input("Nhập y/Y để tiếp tục xóa: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        deleteScoreScreen()

def searchScoreScreen():
    scs = readScores()
    # printScores(scs)

    searchContent = input("Nhập vào để tìm kiếm: ")
    if searchContent == '':
        printScores(scs)
    else:
        stsFilter = []
        for sc in scs:
            if sc['Student_Code'] == searchContent or searchContent == sc['Subject_Code'] :
                stsFilter.append(sc)
        printScores(stsFilter)

    noti = input("Nhập y/Y để tiếp tìm kiếm: ")
    if noti.lower() == 'y':
        # quay lại để nhập tiếp
        searchScoreScreen()

def printScores(scs:list):
    clear_screen()
    printHeader("Danh Sách Điểm Thi")

    print('Mã HV\tTên MH\tĐiểm QT\tĐiểm KT')
    for sc in scs:
        print(f"{sc['Student_Code']}\t{sc['Subject_Code']}\t{sc['processPoint']}\t{sc['endPoint']}")

def statisticalScore():

    sts = readStudents()
    printStatisticalScore(sts)

    noti = input("Nhập t/T để thoát: ")
    if noti.lower() == 't':
        scoreMainScreen()

def printStatisticalScore(sts:list):
    clear_screen()
    printHeader("Danh Sách Thống Kê Điểm Của Học Viên")
    
    sbs = readSubjects()
    scs = readScores()
    print('Mã HV\tHọ tên\tMã MH\tTên MH\tĐiểm QT\tĐiểm KT\tĐiểm TK\tLoại')
    for st in sts:
        idxStudent = st['Code']
        for sb in sbs:
            idxSubject = sb['Code']
            for sc in scs:
                if sc['Student_Code'] == idxStudent and sc['Subject_Code'] == idxSubject:
                    rs = sc
                    quaTrinh = float(rs['processPoint'])
                    ketThuc = float(rs['endPoint'])
                    tongKet = (quaTrinh+ketThuc*2)/3
                    loai = phanLoai(tongKet)
                    print(f"{st['Code']}\t{st['FullName']}\t{sb['Code']}\t{sb['Name']}\t{rs['processPoint']}\t{rs['endPoint']}\t{round(tongKet,2)}\t{loai}")

def xuatFile():
    with open('diem.csv','w',encoding='utf-8',newline = '') as f:
        writer = csv.writer(f,delimiter=',')
        sts = readStudents()
        sbs = readSubjects()
        scs = readScores()
        writer.writerow(['Mã HV','Họ tên','Ngày sinh','Giới tính','Địa chỉ','SĐT','Email','Tên MH','Điểm QT','Điểm KT','Điểm TK'])
        for st in sts:
            idxStudent = st['Code']
            for sb in sbs:
                idxSubject = sb['Code']
                for sc in scs:
                    if sc['Student_Code'] == idxStudent and sc['Subject_Code'] == idxSubject:
                        rs = sc
                        quaTrinh = float(rs['processPoint'])
                        ketThuc = float(rs['endPoint'])
                        tongKet = (quaTrinh+ketThuc*2)/3
                        loai = phanLoai(tongKet)
                        writer.writerow([st['Code'],st['FullName'],st['Birthday'],st['Sex'],st['Address'],st['Phone'],st['Email'],sb['Name'],rs['processPoint'],rs['endPoint'],round(tongKet,2)])
        print("Xuất file thành công!")
    noti = input("Nhập t/T để về màn hình chính: ")
    if noti.lower() == 't':
        scoreMainScreen()
