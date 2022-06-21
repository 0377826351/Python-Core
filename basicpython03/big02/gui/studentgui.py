from bll import StudentBLL
from Utils import print_menu, clear_screen, printHeader
from dto import StudentDTO
import datetime
import re
from tabulate import tabulate


class StudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()

    def studentMenuScreen(self):
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

        try:
            cmd = ''  # mã lệnh người dùng chọn
            while cmd not in ['0', '1', '2', '3', '4']:
                cmd = input("Chức năng: ")

            if cmd == "1":
                # chuyển sang màn hình thêm học viên
                self.addStudentScreen()
                # Quay lại màn hình MENU QLHV(gọi chính nó)
                self.studentMenuScreen()
            if cmd == "2":
                self.editStudentScreen()
                self.studentMenuScreen()
            if cmd == "3":
                self.deleteStudentScreen()
                self.studentMenuScreen()
                pass
            if cmd == "4":
                self.searchStudentScreen()
                self.studentMenuScreen()
            if cmd == "0":
                # trở về màn hình chính
                pass
        except Exception as error:
            print(error)

    def addStudentScreen(self):
        clear_screen()
        printHeader("Thêm Học Viên")

        # nhập dữ liệu từ bàn phím
        while True:
            code = input("Mã Học Viên:")
            if len(code) != 6:
                print("Mã học viên là chuỗi gồm 6 kí tự.")
                continue

            if code[0:2].lower() != 'py':
                print("Hai kí tự đầu tiên phải là 'PY....'")
                continue
            
            isExitst = self.__stBLL.checkExistStudent(code)
            if isExitst == True:
                print("Mã HV đã được sử dụng")
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

        # đổ dữ liệu vào túi "StudentDTO"
        try:
            st = StudentDTO(code,fullName,birthDay,int(sex),address,phone,email)
            self.__stBLL.insert(st)
            print(f"Thêm học viên có mã '{code}' thành công!!")

            noti = input("Nhập y/Y để tiếp tục thêm: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.addStudentScreen()
        except Exception as error:
            print(error)


    def editStudentScreen(self):
        clear_screen()
        printHeader("Chỉnh Sửa Thông Tin Học Viên")

        while True:
            code = input("Mã Học Viên Cần Sửa:")
            if len(code) != 6:
                print("Mã học viên là chuỗi gồm 6 kí tự.")
                continue
            if code[0:2].lower() != 'py':
                print("Hai kí tự đầu tiên phải là 'PY....'")
                continue
            isExitst = self.__stBLL.checkExistStudent(code)
            if isExitst == False:
                print("Mã HV không tồn tại.")
                continue
            break

        #Lấy thông tin theo mã học viên đã nhập
        st = self.__stBLL.getByCode(code)
        print('Họ tên',st.FullName)
        fullName = st.FullName
        noti = input("Nhập y/Y để tiếp tục thêm: ")
        if noti.lower() == 'y':
            # fullName = input("Họ tên mới: ") #không bỏ trống
            while True:
                fullName = input("Họ tên mới:")
                if len(fullName) == 0:
                    print("Bạn cần nhập vào tên của mình.")
                    continue
                break


        print('Ngày sinh',st.BirthDay)
        birthDay = st.BirthDay
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

        print('Giới tính',st.Sex)
        sex = st.Sex
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

        print('Địa chỉ',st.Address)
        address = st.Address
        noti = input("Nhập y/Y để tiếp tục thêm: ")
        if noti.lower() == 'y':
            address = input("Địa chỉ mới: ")

        print('SĐT',st.Phone)
        phone = st.Phone
        noti = input("Nhập y/Y để tiếp tục thêm: ")
        if noti.lower() == 'y':
            # phone = input("SĐT mới: ") #không bỏ trống
            while True:
                phone = input("SĐT m: ")
                if phone.isdigit() == False or len(phone) != 10:
                    print("Số điện thoại chỉ được nhập số và có 10 kí tự.")
                    continue
                break

        print('Email',st.Email)
        email = st.Email
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
        
        try:
            newST = StudentDTO(code,fullName,birthDay,int(sex),address,phone,email)
            rowCount = self.__stBLL.update(newST)
            if rowCount == 0:
                print("Chỉnh sửa thất bại!!!")
            else:
                print(f'Chỉnh sửa học viên có mã "{code}" thành công!!!')

            noti = input("Nhập y/Y để tiếp tục thêm: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.editStudentScreen()
        except Exception as error:
            print(error)
        
    def deleteStudentScreen(self):
        clear_screen()
        printHeader("Xóa Thông Tin Học Viên")

        while True:
            code = input("Mã Học Viên Cần Xóa:")
            if len(code) != 6:
                print("Mã học viên là chuỗi gồm 6 kí tự.")
                continue
            if code[0:2].lower() != 'py':
                print("Hai kí tự đầu tiên phải là 'PY....'")
                continue
            isExitst = self.__stBLL.checkExistStudent(code)
            if isExitst == False:
                print("Mã HV không tồn tại.")
                continue
            break
        
        try:
            rowCount = self.__stBLL.delete(code)
            if rowCount == 0:
                print("Xóa thất bại")
            else:
                print(f'Xóa học viên có mã "{code}" thành công!!!')

            noti = input("Nhập y/Y để tiếp tục xóa: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.deleteStudentScreen()
        except Exception as error:
            print(error)


    def searchStudentScreen(self):
        try:
            sts = self.__stBLL.get()

            searchContent = input("Nội dung tìm kiếm: ")
            if searchContent == '':
                self.printStudents(sts)
            else:
                stsFiltered = self.__stBLL.search(searchContent)
                self.printStudents(stsFiltered)

            noti = input("Nhập y/Y để tiếp tìm kiếm: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.searchStudentScreen()
        except Exception as error:
            print(error)

    def printStudents(self,sts:list):
        clear_screen()
        printHeader("Danh Sách Học Viên")

        table = list(map(lambda st:[st.Code,st.FullName,st.BirthDay,st.Sex,st.Address,st.Phone,st.Email],sts))
        header = ["MaHV","HoTen","Ngày sinh","Giới tính","Địa chỉ","SĐT","Email"]
        print(tabulate(table,header,tablefmt="pretty"))
        
