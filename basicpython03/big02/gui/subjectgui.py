from email import header
from bll import SubjectBLL
from Utils import print_menu, clear_screen, printHeader
from dto import SubjectDTO
from tabulate import tabulate

class SubjectGUI:
    def __init__(self):
        self.__sbBLL = SubjectBLL()

    def subjectMenuScreen(self):
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

        try:
            cmd = ''  # mã lệnh người dùng chọn
            while cmd not in ['0', '1', '2', '3', '4']:
                cmd = input("Chức năng: ")

            if cmd == "1":
                # chuyển sang màn hình thêm môn học
                self.addSubjectScreen()
                # Quay lại màn hình MENU QLHV(gọi chính nó)
                self.subjectMenuScreen()
            if cmd == "2":
                self.editSubjectScreen()
                self.subjectMenuScreen()
            if cmd == "3":
                self.deleteSubjectScreen()
                self.subjectMenuScreen()
            if cmd == "4":
                self.searchSubjectScreen()
                self.subjectMenuScreen()
            if cmd == "0":
                # trở về màn hình chính
                pass
        except Exception as error:
            print(error)

    def addSubjectScreen(self):
        clear_screen()
        printHeader("Thêm Môn Học")
        while True:
            code = input("Mã Môn Học:")
            if len(code) != 6:
                print("Mã môn học là chuỗi gồm 6 kí tự.")
                continue

            if code[0:2].lower() != 'mh':
                print("Hai kí tự đầu tiên phải là 'MH....'")
                continue

            isExitstcode = self.__sbBLL.checkExistSubject(code)
            if isExitstcode == True:
                print("Mã Môn Học đã được sử dụng")
                continue
            break

        while True:
            name = input("Nhập tên môn học: ")
            if len(name) == 0:
                print("Bạn cần nhập vào tên Môn Học mình.")
                continue
            isExistname = self.__sbBLL.checkExistSubjectName(name)
            if isExistname == True:
                print("Tên Môn Học đã được sử dụng")
                continue
            break
        
        try:
            sb = SubjectDTO(code,name)
            self.__sbBLL.insert(sb)
            print(f"Thêm môn học có mã '{code}' thành công!!")

            noti = input("Nhập y/Y để tiếp tục thêm: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.addSubjectScreen()
        except Exception as error:
            print(error)
    
    def editSubjectScreen(self):
        clear_screen()
        printHeader("Chỉnh Sửa Thông Tin Môn Học")

        while True:
            code = input("Mã Môn Học Cần Sửa:")
            if len(code) != 6:
                print("Mã Môn Học là chuỗi gồm 6 kí tự.")
                continue
            if code[0:2].lower() != 'mh':
                print("Hai kí tự đầu tiên phải là 'MH....'")
                continue
            isExitst = self.__sbBLL.checkExistSubject(code)
            if isExitst == False:
                print("Mã MH không tồn tại.")
                continue
            break

        #Lấy thông tin theo mã môn học đã nhập
        sb = self.__sbBLL.getByCode(code)

        print('Tên Môn Học',sb.Name)
        name = sb.Name
        noti = input("Nhập y/Y để sửa tên môn học: ")
        if noti.lower() == 'y':
            while True:
                name = input("Nhập tên môn học mới: ")
                if len(name) == 0:
                    print("Bạn cần nhập vào tên Môn Học mình.")
                    continue
                break
        
        try:
            newsb = SubjectDTO(code,name)
            rowCount = self.__sbBLL.update(newsb)
            if rowCount == 0:
                print("Chỉnh sửa Học Viên thất bại")
            else:
                print('Chỉnh sửa môn học thành công!!!')
            noti = input("Nhập y/Y để tiếp tục sửa: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.editSubjectScreen()
        except Exception as error:
            print(error)

    def deleteSubjectScreen(self):
        clear_screen()
        printHeader("Xóa Thông Tin Môn Học")

        while True:
            code = input("Mã Môn Học cần xóa:")
            if len(code) != 6:
                print("Mã môn học là chuỗi gồm 6 kí tự.")
                continue

            if code[0:2].lower() != 'mh':
                print("Hai kí tự đầu tiên phải là 'MH....'")
                continue

            isExitst = self.__sbBLL.checkExistSubject(code)
            if isExitst == False:
                print("Mã Môn Học không tồn tại")
                continue
            break
        
        try:
            rowCount = self.__sbBLL.delete(code)
            if rowCount == 0:
                print("Xóa môn học thất bại")
            else:
                print(f'Xóa môn học có mã "{code}" thành công!!!')

            noti = input("Nhập y/Y để tiếp tục xóa: ")
            if noti.lower() == 'y':
                # quay lại để nhập tiếp
                self.deleteSubjectScreen()
        except Exception as error:
            print(error)

    def searchSubjectScreen(self):
        try:
            sbs = self.__sbBLL.get()

            searchContent = input("Nội dung tìm kiếm: ")
            if searchContent == '':
                self.printSubjects(sbs)
            else:
                stsFilter = self.__sbBLL.search(searchContent)
                self.printSubjects(stsFilter)

            noti = input("Nhập y/Y để tiếp tìm kiếm: ")
            if noti.lower() == 'y':
                self.searchSubjectScreen()
        except Exception as error:
            print(error)

    def printSubjects(self,sbs:list):
        clear_screen()
        printHeader("Danh Sách Môn Học")

        header = ['Mã MH','Tên MH']
        table = list(map(lambda sub:[sub.Code,sub.Name],sbs))
        print(tabulate(table,header,tablefmt="pretty"))