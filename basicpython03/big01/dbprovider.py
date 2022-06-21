# giao tiếp dữ liệu vào ra từ DB

studentPath = "database/students.txt"
subjectPath = "database/subjects.txt"
scorePath = "database/scores.txt"

# st = {
#     'Code':'PY03.1',
#     'FullName':'Nguyễn Tuấn Minh',
#     'Birthday':'19/12/2000',
#     'Sex':0,
#     'Address':'Hà Nam',
#     'Phone':'0333826355',
#     'Email':'nguyentuanminh3120@gmail.com'
# }


def writeStudent(st: dict):
    with open(studentPath, 'a', encoding='utf-8') as f:
        line = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
        f.write(line)

def writeStudents(sts: list):
    with open(studentPath, 'w', encoding='utf-8') as f:
        for st in sts:
            line = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
            f.write(line)


def readStudents():
    sts = []
    try:
        with open(studentPath, 'r', encoding='utf-8') as f:
            for line in f:
                value = line.strip().split('|')
                st = {
                    'Code': value[0],
                    'FullName': value[1],
                    'Birthday': value[2],
                    'Sex': value[3],
                    'Address': value[4],
                    'Phone': value[5],
                    'Email': value[6]
                }
                sts.append(st)
    except:
        with open(studentPath, 'w', encoding='utf-8') as f:
            f.write('')
    return sts

def getStudentByCode(code:str):
    rs = None
    sts = readStudents()
    for st in sts:
        if st['Code'] == code:
            rs = st
            break
    return rs

def checkExistStudent(code: str):
    isExist = False
    # lấy ra toàn bộ học viên trong DB
    sts = readStudents()
    for st in sts:
        if st['Code'] == code:
            isExist = True
            break
    return isExist


def writeSubject(sub: dict):
    with open(subjectPath, 'a', encoding='utf-8') as f:
        line = f"{sub['Code']}|{sub['Name']}\n"
        f.write(line)


def writeSubjects(subs: dict):
    with open(subjectPath, 'w', encoding='utf-8') as f:
        for sub in subs:
            line = f"{sub['Code']}|{sub['Name']}\n"
            f.write(line)


def readSubjects():
    subs = []
    try:
        with open(subjectPath, 'r', encoding='utf-8') as f:
            for line in f:
                value = line.strip().split("|")
                sub = {
                    'Code': value[0],
                    'Name': value[1]
                }
                subs.append(sub)
    except:
        with open(studentPath, 'w', encoding='utf-8') as f:
            f.write('')
    return subs

def getSubjectByCode(code:str):
    rs = None
    sts = readSubjects()
    for st in sts:
        if st['Code'] == code:
            rs = st
            break
    return rs

def checkExistSubject(code: str):
    isExist = False
    # lấy ra toàn bộ môn học trong DB
    sbs = readSubjects()
    for sb in sbs:
        if sb['Code'] == code:
            isExist = True
            break
    return isExist

def checkExistSubjectName(name: str):
    isExist = False
    # lấy ra toàn bộ môn học trong DB
    sbs = readSubjects()
    for sb in sbs:
        if sb['Name'] == name:
            isExist = True
            break
    return isExist


def writeScore(sc: dict):
    with open(scorePath, 'a', encoding='utf-8') as f:
        line = f"{sc['Student_Code']}|{sc['Subject_Code']}|{sc['processPoint']}|{sc['endPoint']}\n"
        f.write(line)


def writeScores(scs: list):
    with open(scorePath, 'w', encoding='utf-8') as f:
        for sc in scs:
            line = f"{sc['Student_Code']}|{sc['Subject_Code']}|{sc['processPoint']}|{sc['endPoint']}\n"
            f.write(line)


def readScores():

    scs = []
    try:
        with open(scorePath, 'r', encoding='utf-8') as f:
            for line in f:
                value = line.strip().split('|')
                sc = {
                    'Student_Code': value[0],
                    'Subject_Code': value[1],
                    'processPoint': value[2],
                    'endPoint': value[3]
                }
                scs.append(sc)
    except:
        with open(studentPath, 'w', encoding='utf-8') as f:
            f.write('')
    return scs

def checkExistScore(studentCode: str,subjectCode:str):  
    isExist = False
    # lấy ra toàn bộ điểm trong DB
    scs = readScores()
    for sc in scs:
        if sc['Student_Code'] == studentCode and sc['Subject_Code'] == subjectCode:
            isExist = True
            break
    return isExist


def getScoreByCode(studentCode:str,subjectCode:str):
    #TODO
    rs = None
    scs = readScores()
    for sc in scs:
        if sc['Student_Code'] == studentCode and sc['Subject_Code'] == subjectCode:
            rs = sc
            break
    return rs

def phanLoai(diem):
    if diem >=9 and diem <= 10:
        return 'A'
    if diem >=7 and diem <9:
        return 'B'
    if diem >= 5 and diem <7:
        return 'C'
    if diem < 5 :
        return 'D'