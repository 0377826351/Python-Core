# Main module của chương trình
from utils import print_menu, clear_screen, printHeader
from studentman import studentMainScreen
from subjectman import subjectMainScreen
from scoreman import scoreMainScreen

# Màn hình chính của chương trình


def mainMenuScreen():
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
        # chuyển sang QLHV
        studentMainScreen()
        # quay về MHC
        mainMenuScreen()
    if cmd == "2":
        subjectMainScreen()
        mainMenuScreen()
    if cmd == "3":
        scoreMainScreen()
        mainMenuScreen()
    if cmd == "0":
        print("Kết thúc chương trình.")
        exit()


if __name__ == '__main__':
    mainMenuScreen()
