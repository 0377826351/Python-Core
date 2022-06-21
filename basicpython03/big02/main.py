from gui import StudentGUI,SubjectGUI,ScoreGUI
from Utils import print_menu, clear_screen, printHeader


class MainGUI:
    def __init__(self):
        self.__stGUI = StudentGUI()
        self.__sbGUI = SubjectGUI()
        self.__scGUI = ScoreGUI()

    def mainMenuScreen(self):
        clear_screen()
        printHeader('Quản lý điểm thi')
        funcs = [
            '1. Quản lý học viên',
            '2. Quản lý môn học',
            '3. Quản lý điểm thi',
            '0. Thoát'
        ]
        print_menu(funcs)

        cmd = ''  # mã lệnh người dùng chọn
        while cmd not in ['0', '1', '2', '3']:
            cmd = input("Chức năng: ")

        if cmd == "1":
            self.__stGUI.studentMenuScreen()
            self.mainMenuScreen()
        if cmd == "2":
            self.__sbGUI.subjectMenuScreen()
            self.mainMenuScreen()
        if cmd == "3":
            self.__scGUI.scoreMenuScreen()
            self.mainMenuScreen()
        if cmd == "0":
            print("Kết thúc chương trình.")
            exit()


if __name__ == '__main__':
    mainGUI = MainGUI()
    mainGUI.mainMenuScreen()
