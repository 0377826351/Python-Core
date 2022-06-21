from dto import ScoreDTO,DataDTO
from .dbprovider import DBProvider

class ScoreDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        sql  = '''
            CREATE TABLE IF NOT EXISTS Scores(
                CodeST VARCHAR(6) REFERENCES Students(Code) ON DELETE CASCADE,
                CodeSB VARCHAR(6) REFERENCES Subjects(Code) ON DELETE CASCADE,
                ProcessPoint FLOAT,
                EndPoint FLOAT,
                PRIMARY KEY (CodeST, CodeSB)
            );
        '''
        self.__dbProvider.exec(sql)

    def insert(self,sc:ScoreDTO):
        rowCount = 0
        try:
            sql = '''
                INSERT INTO Scores(CodeST,CodeSB,ProcessPoint,EndPoint)
                VALUES(%s,%s,%s,%s)
            '''
            params = (sc.CodeST,sc.CodeSB,sc.ProcessPoint,sc.EndPoint)
            rowCount = self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    def update(self,sc:ScoreDTO):
        rowCount = 0
        try:
            sql = '''
                UPDATE Scores 
                SET 
                    ProcessPoint = %s,
                    EndPoint = %s
                WHERE
                    CodeST = %s AND
                    CodeSB = %s
            '''
            params = (sc.ProcessPoint,sc.EndPoint,sc.CodeST,sc.CodeSB)
            rowCount = self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    def delete(self,codeST:str,codeSB:str):
        rowCount = 0
        try:
            sql = '''
                DELETE FROM Scores
                WHERE CodeST = %s AND
                    CodeSB = %s
            '''
            params = (codeST,codeSB)
            rowCount =  self.__dbProvider.exec(sql,params)
        except Exception as error:
            print(error)
        return rowCount

    def get(self):
        scDtos = []
        try:
            sql = '''SELECT * FROM Scores
                    '''
            scs = self.__dbProvider.get(sql)
            scDtos = list(map(lambda sc:ScoreDTO(sc[0],sc[1],sc[2],sc[3]),scs))
        except Exception as error:
            print(error)
        finally:
            return scDtos

    def getByCode(self,codeST: str,codeSB:str):
        scDto = None
        try:
            sql = '''
                SELECT * FROM Scores
                WHERE CodeST = %s AND
                    CodeSB = %s
            '''
            params = (codeST,codeSB)
            sc = self.__dbProvider.getOne(sql, params)
            # chuyển tupple sang StudentDTO
            scDto = ScoreDTO(sc[0],sc[1],sc[2],sc[3])
        except Exception as error:
            print(error)
        finally:
            return scDto

    #Tìm kiếm
    def search(self,text:str):
        scDtos = []
        try:
            sql = '''
                SELECT * FROM Scores
                WHERE CodeST = %s
                    OR CodeSB = %s
            '''
            params = (text,text)
            scs = self.__dbProvider.get(sql,params)
            scDtos = list(map(lambda sc:ScoreDTO(sc[0],sc[1],sc[2],sc[3]),scs))
        except Exception as error:
            print(error)
        finally:
            return scDtos

    def checkExistScore(self,codeST: str,codeSB:str):
        sql = '''
            SELECT * FROM Scores
            WHERE CodeST = %s AND 
                CodeSB = %s
        '''
        params = (codeST,codeSB)
        st = self.__dbProvider.getOne(sql, params)
        return st is not None
    
    def data(self):
        dtsDTOs = []
        try:
            sql = '''
                SELECT CodeST,FullName,BirthDay,Sex,Address,Phone,Email,CodeSB,ProcessPoint,EndPoint,round((ProcessPoint + EndPoint*2)/3,2),
                CASE 
                    WHEN (ProcessPoint+EndPoint*2)/3 >= 9 AND (ProcessPoint+EndPoint*2)/3 <= 10 THEN 'A'
                    WHEN (ProcessPoint+EndPoint*2)/3 >= 7 AND (ProcessPoint+EndPoint*2)/3 < 9 THEN 'B'
                    WHEN (ProcessPoint+EndPoint*2)/3 >= 5 AND (ProcessPoint+EndPoint*2)/3 < 7 THEN 'C'
                    ELSE 'D'
                END `Rank`
                FROM Scores sc
                JOIN Students st ON sc.CodeST = st.Code
                JOIN Subjects sb ON sc.CodeSB = sb.Code
            '''
            dts = self.__dbProvider.get(sql)
            dtsDTOs = list(map(lambda dt:DataDTO(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11]),dts))
        except Exception as error:
            print(error)
        finally:
            return dtsDTOs

