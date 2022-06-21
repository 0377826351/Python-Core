#các công cụ hỗ trợ dự án
import os
import openpyxl

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

# xuất file excel
def output_Excel(input_detail,output_excel_path):
        #Xác định số hàng và cột lớn nhất trong file excel cần tạo
        row = len(input_detail)
        column = len(input_detail[0])

        #Tạo một workbook mới và active nó
        wb = openpyxl.Workbook()
        ws = wb.active
        
        #Dùng vòng lặp for để ghi nội dung từ input_detail vào file Excel
        for i in range(0,row):
            for j in range(0,column):
                v=input_detail[i][j]
                ws.cell(column=j+1, row=i+1, value=v)

        #Lưu lại file Excel
        wb.save(output_excel_path)