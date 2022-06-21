# # B1
# string = input("Nhập vào một chuỗi bất kì: ")
# count = 0
# for i in string:
#     if i == "t" or i == "T":
#         count += 1
# print(f"Số lần xuất hiện của 't' và 'T' là : {count}")

# #B2
# is_valid = input(("Nhập string: "))
# correct_length = False
# has_uppercase = False
# has_lowercase = False
# has_digit = False
# if (len(is_valid) >= 7):
#     correct_length = True
#     for i in is_valid:
#         if i.upper():
#             has_uppercase = True
#     for i in is_valid:
#         if i.islower():
#             has_lowercase = True
#     for i in is_valid:
#         if i.isdigit():
#             has_digit = True
# if correct_length and has_uppercase and has_lowercase and has_digit:
#     is_valid = True
# else:
#     is_valid = False
# print(is_valid)

# # B3
# list_02 = [3, 2, 1]
# list_02.append(input('Nhap chuoi:'))
# print(list_02)
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)