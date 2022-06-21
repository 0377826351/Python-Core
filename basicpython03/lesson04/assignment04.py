# B1
print("Bắt đầu hướng dẫn")

def fuc_step1(kw01):
    if kw01 == '':
        print("Step 1: Unplug the dryer and move it away from the wall.")
    else:
        fuc_step1(input("Bạn nhập sai rồi nhập lại đi: "))

def fuc_step2(kw02):
    if kw02 == '':
        print("Step 2: Remove the six screws from the back of the dryer.")
    else:
        fuc_step2(input("Bạn nhập sai rồi nhập lại đi: "))
    
def fuc_step3(kw03):
    if kw03 == '':
        print("Step 3: Remove the dryer’s back panel.")
    else:
        fuc_step3(input("Bạn nhập sai rồi nhập lại đi: "))

def fuc_step4(kw04):
    if kw04 == '':
        print("Step 4: Pull the top of the dryer straight up.")
    else:
        fuc_step4(input("Bạn nhập sai rồi nhập lại đi: "))

fuc_step1(input("Press Enter to see the next step: "))
fuc_step2(input("Press Enter to see the next step: "))
fuc_step3(input("Press Enter to see the next step: "))
fuc_step4(input("Press Enter to see the next step: "))


# B2
def reverse_name(first_name,last_name):
    print(last_name,first_name)
first_name = 'Minh'
last_name = 'Nguyen'
reverse_name(first_name,last_name) # position
reverse_name(last_name=last_name, first_name=first_name) # keyword

# B3 
def main():
    hours = int(input("How many hours did you work: "))
    pay_rate = float(input('Enter your hourly pay rate: '))
    gross_pay = hours * pay_rate
    print(f'Gross pay: {gross_pay:.2f}')

main()

# B4   
# What will the following code display?
try:
    x = float('ab1')
    print("the conversion is complete")
except IOError:
    print('This code coused an IOError')
except ValueError:
    print('This code caused a ValueError')
    print('The end')
# ===========> Hiển thị 2 dòng value error do bắt chính xác ngoại lệ

# What will the following code display?
try:
    x = float('ab1')
    print(x)
except IOError:
    print('This code coused an IOError')
except ZeroDivisionError:
    print('This code coused an ZeroDivisionError')
except:
    print('An error happened')
    print('The end')

#===========> Hiển thị ra hai dòng trong except mà không bắt chính xác ngoại lệ do 2 except bắt chính xác ngoại lệ không đúng