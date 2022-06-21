#các công cụ hỗ trợ dự án
import os

#xóa rác trong cmd
def clear_screen():
    os.system('cls||clear')

#in ra menu
def print_menu(chuc_nang: list):
    print("\n".join(chuc_nang))

#in ra tiêu đề
def printHeader(title: str):
    header = f'***{title}***'
    print(header)
    print('-'*len(header))
