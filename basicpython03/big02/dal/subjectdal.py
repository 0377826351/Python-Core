from dto import SubjectDTO
from .dbprovider import DBProvider

class SubjectDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        sql  = '''
            CREATE TABLE IF NOT EXISTS Subjects(
                Code VARCHAR(6) PRIMARY KEY,
                Name VARCHAR(30)
            );
        '''
        self.__dbProvider.exec(sql)

    def insert(self,sb:SubjectDTO):
        rowCount = 0
        try:
            sql = '''
                INSERT INTO Subjects(Code,Name)
                VALUES(%s,%s)
            '''
            params = (sb.Code,sb.Name)
            rowCount = self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    def update(self,sb:SubjectDTO):
        rowCount = 0
        try:
            sql = '''
                UPDATE Subjects 
                SET 
                    Name = %s
                WHERE
                    Code = %s
            '''
            params = (sb.Name,sb.Code)
            rowCount = self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    def delete(self,code:str):
        rowCount = 0
        try:
            sql = '''
                DELETE FROM Subjects
                WHERE Code = %s
            '''
            params = (code,)
            rowCount = self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    def get(self):
        sbDtos = None
        try:
            sql = '''SELECT * FROM Subjects'''
            sbs = self.__dbProvider.get(sql)
            sbDtos = list(map(lambda sb:SubjectDTO(sb[0],sb[1]),sbs))
        except Exception as error:
            print(error)
        finally:
            return sbDtos

    def getByCode(self,code: str):
        sbDto = None
        try:
            sql = '''
                SELECT * FROM Subjects
                WHERE Code = %s
            '''
            params = (code,)
            sb = self.__dbProvider.getOne(sql, params)
            # chuyển tupple sang StudentDTO
            sbDto = SubjectDTO(sb[0],sb[1])
        except Exception as error:
            print(error)
        finally:
            return sbDto

    #Tìm kiếm
    def search(self,text:str):
        sbDtos = None
        try:
            sql = '''
                SELECT * FROM Subjects
                WHERE Code = %s
                    OR Name LIKE %s
            '''
            params = (text,f'%{text}%')
            sbs = self.__dbProvider.get(sql,params)
            sbDtos = list(map(lambda st:SubjectDTO(st[0],st[1]),sbs))
        except Exception as error:
            print(error)
        finally:
            return sbDtos

    def checkExistSubject(self,code: str):
        sql = '''
            SELECT * FROM Subjects
            WHERE Code = %s
        '''
        params = (code,)
        sb = self.__dbProvider.getOne(sql, params)
        return sb is not None
    
    def checkExistSubjectName(self,name: str):
        sql = '''
            SELECT * FROM Subjects
            WHERE Name = %s
        '''
        params = (name,)
        sb = self.__dbProvider.getOne(sql, params)
        return sb is not None

