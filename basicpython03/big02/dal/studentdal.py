from .dbprovider import DBProvider
from dto import StudentDTO
import unittest


class StudentDAL:
    def __init__(self):
        # khởi tạo object DBProvider để giao tiếp với Data gián tiếp qua DBProvider
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        sql  = '''
            CREATE TABLE IF NOT EXISTS Students(
                Code VARCHAR(6) PRIMARY KEY,
                FullName NVARCHAR(50),
                Birthday VARCHAR(20),
                Sex TINYINT(1),
                Address NVARCHAR(500),
                Phone VARCHAR(20),
                Email VARCHAR(250)
            );
        '''
        self.__dbProvider.exec(sql)

    #Thêm
    def insert(self,st:StudentDTO):
        rowCount = 0
        try:
            sql = '''
                INSERT INTO Students(Code,FullName,BirthDay,Sex,Address,Phone,Email)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
            '''
            params = (st.Code,st.FullName,st.BirthDay,st.Sex,st.Address,st.Phone,st.Email)
            rowCount =  self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    #Sửa
    def update(self,st:StudentDTO):
        rowCount = 0
        try:
            sql = '''
                UPDATE Students 
                SET 
                    FullName = %s,
                    BirthDay = %s,
                    Sex = %s,
                    Address = %s,
                    Phone = %s,
                    Email = %s
                WHERE
                    Code =%s
            '''
            params = (st.FullName,st.BirthDay,st.Sex,st.Address,st.Phone,st.Email,st.Code)
            rowCount = self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    #xóa
    def delete(self,code:str):
        rowCount = 0
        try:
            sql = '''
                DELETE FROM Students
                WHERE Code = %s
            '''
            params = (code,)
            rowCount =  self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount
    #lấy tất cả dữ liệu
    def get(self):
        stDtos = []
        try:
            sql = '''SELECT * FROM Students'''
            sts = self.__dbProvider.get(sql)
            stDtos = list(map(lambda st:StudentDTO(st[0],st[1],st[2],st[3],st[4],st[5],st[6]),sts))
        except Exception as error:
            print(error)
        finally:
            return stDtos

    #lấy 1 bản ghi theo code
    def getByCode(self,code: str):
        stDto = []
        try:
            sql = '''
                SELECT * FROM Students
                WHERE Code = %s
            '''
            params = (code,)
            st = self.__dbProvider.getOne(sql, params)
            # chuyển tupple sang StudentDTO
            stDto = StudentDTO(st[0],st[1],st[2],st[3],st[4],st[5],st[6]) if st is not None else None
        except Exception as error:
            print(error)
        finally:
            return stDto

    #Tìm kiếm
    def search(self,text:str):
        stDtos = []
        try:
            sql = '''
                SELECT * FROM Students
                WHERE Code = %s
                    OR FullName LIKE %s
                    OR Email LIKE %s
            '''
            params = (text,f'%{text}%',f'%{text}%')
            sts = self.__dbProvider.get(sql,params)
            stDtos = list(map(lambda st:StudentDTO(st[0],st[1],st[2],st[3],st[4],st[5],st[6]),sts))
        except Exception as error:
            print(error)
        finally:
            return stDtos

    def checkExistStudent(self,code: str):
        sql = '''
            SELECT * FROM Students
            WHERE Code = %s
        '''
        params = (code,)
        st = self.__dbProvider.getOne(sql, params)
        return st is not None



# Kịch bản test
class StudentDALTest(unittest.TestCase):
    def setUp(self):
        self.__stDAL = StudentDAL()

    def testCheckExistsIsTrue(self):
        # Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2001', 1, 'Test', '9999999999', 'test@test.test')
        self.__stDAL.insert(st)
        expectedResult = True

        # Act
        actualResutl = self.__stDAL.checkExistStudent(st.Code)

        # Assert
        self.assertEqual(expectedResult, actualResutl)

        # Teardown for this test case
        self.__stDAL.delete(st.Code)

    def testGetByCodeIsNotNone(self):
        # Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2001', 1, 'Test', '9999999999', 'test@test.test')
        self.__stDAL.insert(st)
        expectedResult = st

        # Act
        actualResult = self.__stDAL.getByCode(st.Code)

        # Assert
        # self.assertEqual(expectedResult, actualResult) # Không đúng vì là 2 đối tượng khác nhau, mặc dù các thuộc tính = nhau nhưng 2 đối tượng vẫn không = nhau đc
        self.assertEqual(expectedResult.Code, actualResult.Code)
        self.assertEqual(expectedResult.FullName, actualResult.FullName)
        self.assertEqual(expectedResult.BirthDay, actualResult.BirthDay)
        self.assertEqual(expectedResult.Sex, actualResult.Sex)
        self.assertEqual(expectedResult.Address, actualResult.Address)
        self.assertEqual(expectedResult.Phone, actualResult.Phone)
        self.assertEqual(expectedResult.Email, actualResult.Email)

        # Teardown for this test case
        self.__stDAL.delete(st.Code)

    def testGetByCodeIsNone(self):
        # Arrange
        codeNotExists = 'PY9999' # Đây là mã không tồn tại trong DB
        expectedResult = None

        # Act
        actualResutl = self.__stDAL.getByCode(codeNotExists)

        # Assert
        self.assertEqual(expectedResult, actualResutl)

    def testDeleteComplete(self):
        # Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2001', 1, 'Test', '9999999999', 'test@test.test')
        self.__stDAL.insert(st)
        expectedResult = 1

        # Act
        actualResutl = self.__stDAL.delete(st.Code)

        # Assert
        self.assertEqual(expectedResult, actualResutl)

        # Teardown for this test case

    def testInsertComplete(self):
        # Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2001', 1, 'Test', '9999999999', 'test@test.test')
        expectedResult = True

        # Act
        actualResutl = self.__stDAL.insert(st)

        # Assert
        self.assertEqual(expectedResult, actualResutl)

        # Teardown for this test case
        self.__stDAL.delete(st.Code)

    def testUpdateFailed(self):
        # Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2001', '1', 'Test', '9999999999', 'test@test.test')
        expectedResult = False

        # Act
        actualResutl = self.__stDAL.update(st)

        # Assert
        self.assertEqual(expectedResult, actualResutl)

        # Teardown for this test case
    # TODO ...

    def tearDown(self):
        pass