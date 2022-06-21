import json
import sys
print(sys.getdefaultencoding())

# # #Đọc file
# f = open("a.txt",'r',encoding='utf-8')
# text = f.read()
# print(text)
# f.close()

# #ghi file nếu file tồn tại sẽ tạo 1 file mới rồi viết lại từ đầu
# f = open("a.txt",'w',encoding='utf-8')
# text = f.write("xin chào")
# f.close()

# #ghi file nếu file tồn tại sẽ viết tiếp vào cuối file
# f = open("a.txt",'a',encoding='utf-8')
# text = f.write("xin chào")
# f.close()

# # 1 cách mở file khác và nó tự động đóng file
# with open("a.txt",'r',encoding='utf-8') as f:
#     pass

listHV = [
    {
        'Ten': "Ming",
        'gioitinh': "Nam"
    },
    {
        'Ten': "Mingg",
        'gioitinh': "Nu"
    }
]
with open("a.json", 'w', encoding='utf-8') as f:
    json.dump(listHV, f, ensure_ascii=False, indent=4)

with open("a.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
