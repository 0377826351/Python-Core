from bll import ScoreBLL,StudentBLL,SubjectBLL
from dto import ScoreDTO
from Utils import print_menu, clear_screen, printHeader,output_Excel
from tabulate import tabulate


class ScoreGUI:
    def __init__(self):
        self.__scBLL = ScoreBLL()
        self.__stBLL = StudentBLL()
        self.__sbBLL = SubjectBLL()

    def scoreMenuScreen(self):
        clear_screen()
        printHeader("Quản Lý Điểm Thi")

        funcs = [
            '1. Thêm',
            '2. Sửa',
            '3. Xóa',
            '4. Tìm kiếm',
            '5. Thống kê',
            '6. Xuất ra file Excel',
            '0. Trở về'
        ]
        print_menu(funcs)

        try:
            cmd = ''  # mã lệnh người dùng chọn
            while cmd not in ['0', '1', '2', '3', '4', '5','6']:
                cmd = input("Chức năng: ")

            if cmd == "1":
                # chuyển sang màn hình thêm điểm thi
                self.addScoreSubject()
                # Quay lại màn hình MENU QLHV(gọi chính nó)
                self.scoreMenuScreen()
            if cmd == "2":
                self.editScoreScreen()
                self.scoreMenuScreen()
            if cmd == "3":
                self.deleteScoreScreen()
                self.scoreMenuScreen()
            if cmd == "4":
                self.searchScoreScreen()
                self.scoreMenuScreen()
            if cmd == "5":
                self.statisticalScore()
                self.scoreMenuScreen()
            if cmd == '6':
                self.xuatFile()
                self.scoreMenuScreen()
            if cmd == "0":
                # trở về màn hình chính
                pass
        except Exception as error:
            print(error)

    def addScoreSubject(self):
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

                if studentCode[0:2].lower() != 'py':
                    print("Hai kí tự đầu tiên phải là 'PY....'")
                    continue

                isExitst = self.__stBLL.checkExistStudent(studentCode)
                if isExitst == False:
                    print("Mã HV không tồn tại")
                    continue
                break

            while True:
                subjectCode = input("Nhập mã môn học: ")
                if len(subjectCode) != 6:
                    print("Mã môn học là chuỗi gồm 6 kí tự.")
                    continue

                if subjectCode[0:2].lower() != 'mh':
                    print("Hai kí tự đầu tiên phải là 'MH....'")
                    continue

                isExitst = self.__sbBLL.checkExistSubject(subjectCode)
                if isExitst == False:
                    print("Mã Môn Học không tồn tại")
                    continue
                break

            isExitstScore = self.__scBLL.checkExistScore(studentCode,subjectCode)
            if isExitstScore == True:
                print("Điểm của môn học đã có.")
                continue
            break
        
        while True:
            processPoint = input("Nhập điểm quá trình: ")
            if processPoint == '':
                print("Không được để trống điểm.")
                continue
            if processPoint.isdecimal() == False:
                print("Điểm phải là số thập phân!")
                continue
            if float(processPoint) < 0 or float(processPoint) >10:
                print("Nhập lại điểm (0-10).")
                continue
            break
        
        while True:
            endPoint = input("Nhap điểm kết thúc: ")
            if endPoint == '':
                print("Không được để trống điểm.")
                continue
            if endPoint.isdecimal() == False:
                print("Điểm phải là số thập phân!")
                continue
            if float(endPoint) < 0 or float(endPoint) > 10:
                print("Nhập lại điểm (0-10).")
                continue
            break
        
        try:
            sc = ScoreDTO(studentCode,subjectCode,processPoint,endPoint)
            self.__scBLL.insert(sc)
            print("Thêm điểm thành công!!")

        except Exception as error:
            print(error)
        noti = input("Nhập y/Y để tiếp tục thêm: ")
        if noti.lower() == 'y':
            # quay lại để nhập tiếp
            self.addScoreSubject()

    def editScoreScreen(self):
        clear_screen()
        printHeader("Chỉnh Sửa Thông Tin Điểm")

        while True:
            studentCode = None
            subjectCode = None
            while True:
                studentCode = input("Nhập mã học viên: ")
                if len(studentCode) != 6:
                    print("Mã học viên là chuỗi gồm 6 kí tự.")
                    continue

                if studentCode[0:2].lower() != 'py':
                    print("Hai kí tự đầu tiên phải là 'PY....'")
                    continue

                isExitst = self.__stBLL.checkExistStudent(studentCode)
                if isExitst == False:
                    print("Mã HV không tồn tại")
                    continue
                break

            while True:
                subjectCode = input("Nhập mã môn học: ")
                if len(subjectCode) != 6:
                    print("Mã môn học là chuỗi gồm 6 kí tự.")
                    continue

                if subjectCode[0:2].lower() != 'mh':
                    print("Hai kí tự đầu tiên phải là 'MH....'")
                    continue

                isExitst = self.__sbBLL.checkExistSubject(subjectCode)
                if isExitst == False:
                    print("Mã Môn Học không tồn tại")
                    continue
                break

            isExitstScore = self.__scBLL.checkExistScore(studentCode,subjectCode)
            if isExitstScore == False:
                print("Điểm của học viên chưa có.")
                continue
            break

        sc = self.__scBLL.getByCode(studentCode,subjectCode)

        print('Điểm quá trình:',sc.ProcessPoint)
        processPoint = sc.ProcessPoint
        noti = input("Nhập y/Y để tiếp tục thêm: ")
        if noti.lower() == 'y':
            while True:
                processPoint = input("Nhập điểm quá trình mới: ")
                if processPoint == '':
                    print("Không được để trống điểm.")
                    continue
                if processPoint.isdecimal() == False:
                    print("Điểm phải là số thập phân!")
                    continue
                if float(processPoint) < 0 or float(processPoint) >10:
                    print("Nhập lại điểm (0-10).")
                    continue
                break

        print('Điểm kết thúc:',sc.EndPoint)
        endPoint = sc.EndPoint
        noti = input("Nhập y/Y để tiếp tục thêm: ")
        if noti.lower() == 'y':
            while True:
                endPoint = input("Nhập điểm kết thúc mới: ")
                if endPoint == '':
                    print("Không được để trống điểm.")
                    continue
                if endPoint.isdecimal() == False:
                    print("Điểm phải là số thập phân!")
                    continue
                if float(endPoint) < 0 or float(endPoint) > 10:
                    print("Nhập lại điểm (0-10).")
                    continue
                break
        
        try:
            newSC = ScoreDTO(studentCode,subjectCode,processPoint,endPoint)
            rowCount = self.__scBLL.update(newSC)
            if rowCount == 0:
                print("Chỉnh sửa điểm thất bại!")
            else:
                print('Chỉnh sửa điểm thành công!!!')
            noti = input("Nhập y/Y để tiếp tục thêm: ")
        except Exception as error:
            print(error)
        if noti.lower() == 'y':
            # quay lại để nhập tiếp
            self.editScoreScreen()

    def deleteScoreScreen(self):
        clear_screen()
        printHeader("Xóa Thông Tin Điểm")

        while True:
            studentCode = None
            subjectCode = None
            while True:
                studentCode = input("Nhập mã học viên: ")
                if len(studentCode) != 6:
                    print("Mã học viên là chuỗi gồm 6 kí tự.")
                    continue

                if studentCode[0:2].lower() != 'py':
                    print("Hai kí tự đầu tiên phải là 'PY....'")
                    continue

                isExitst = self.__stBLL.checkExistStudent(studentCode)
                if isExitst == False:
                    print("Mã HV không tồn tại")
                    continue
                break

            while True:
                subjectCode = input("Nhập mã môn học: ")
                if len(subjectCode) != 6:
                    print("Mã môn học là chuỗi gồm 6 kí tự.")
                    continue

                if subjectCode[0:2].lower() != 'mh':
                    print("Hai kí tự đầu tiên phải là 'MH....'")
                    continue

                isExitst = self.__sbBLL.checkExistSubject(subjectCode)
                if isExitst == False:
                    print("Mã Môn Học không tồn tại")
                    continue
                break

            isExitstScore = self.__scBLL.checkExistScore(studentCode,subjectCode)
            if isExitstScore == False:
                print("Điểm của học viên chưa có.")
                continue
            break
        
        try:
            rowCount = self.__scBLL.delete(studentCode,subjectCode)
            if rowCount == 0:
                print("Xóa học viên thất bại")
            else:
                print(f'Xóa điểm thành công!!!')

        except Exception as error:
            print(error)
        noti = input("Nhập y/Y để tiếp tục xóa: ")
        if noti.lower() == 'y':
            # quay lại để nhập tiếp
            self.deleteScoreScreen()

    def searchScoreScreen(self):
        try:
            scs = self.__scBLL.get()

            searchContent = input("Nhập vào để tìm kiếm: ")
            if searchContent == '':
                self.printScores(scs)
            else:
                scsFiltered = self.__scBLL.search(searchContent)
                self.printScores(scsFiltered)

        except Exception as error:
            print(error)
        noti = input("Nhập y/Y để tiếp tìm kiếm: ")
        if noti.lower() == 'y':
            # quay lại để nhập tiếp
            self.searchScoreScreen()

    def printScores(self,scs:list):
        clear_screen()
        printHeader("Danh Sách Điểm Thi")

        header = ['Mã HV','Tên MH','Điểm QT','Điểm KT']
        table = list(map(lambda sc:[sc.CodeST,sc.CodeSB,sc.ProcessPoint,sc.EndPoint],scs))
        print(tabulate(table,header,tablefmt="pretty"))

    def statisticalScore(self):
        clear_screen()
        printHeader("Danh Sách Thống Kê Điểm Của Học Viên")
        stas = self.__scBLL.data()
        header = ['Mã MH','Tên MH','Điểm QT','Điểm KT','Điểm TK','Loại']
        table = list(map(lambda sta:[sta.CodeST,sta.CodeSB,sta.ProcessPoint,sta.EndPoint,sta.FinalGrade,sta.Rank],stas))
        print(tabulate(table,header,tablefmt="pretty"))

        while True:
            noti = input("Nhập t/T để thoát: ")
            if noti.lower() != 't':
                continue
            break

    def xuatFile(self):
        totalsDTO = self.__scBLL.data()
        totals = list(map(lambda totalDTO: [totalDTO.CodeST, 
                                            totalDTO.FullName, totalDTO.BirthDay, 
                                            totalDTO.Sex, totalDTO.Address, 
                                            totalDTO.Phone, totalDTO.Email, 
                                            totalDTO.CodeSB, totalDTO.ProcessPoint, 
                                            totalDTO.EndPoint, totalDTO.FinalGrade, 
                                            totalDTO.Rank],totalsDTO))
        excel = totals.copy()
        excel.insert(0, ['Mã học viên', 'Họ tên', 'Ngày sinh', 
                    'Giới tính', 'Địa chỉ', 'Số điện thoại', 
                    'Email', 'Tên môn học', 'Điểm quá trình', 
                    'Điểm kết thúc', 'Điểm tổng kết', 'Rank'])
        output_excel_path = 'dt.xlsx'
        output_Excel(excel,output_excel_path)

        print("Xuất file thành công!")
        while True:
            noti = input("Nhập t/T để thoát: ")
            if noti.lower() != 't':
                continue
            break






