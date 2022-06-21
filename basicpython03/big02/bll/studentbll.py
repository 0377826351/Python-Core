from dal import StudentDAL
from dto import StudentDTO

class StudentBLL:
    def __init__(self):
        self.__stDAL = StudentDAL()

    def insert(self,st:StudentDTO):
        return self.__stDAL.insert(st)

    def update(self,st:StudentDTO):
        return self.__stDAL.update(st)

    def delete(self,code:str):
        return self.__stDAL.delete(code)

    def get(self):
        return self.__stDAL.get()

    def getByCode(self,code: str):
        return self.__stDAL.getByCode(code)
        
    def search(self,text:str):
        return self.__stDAL.search(text)

    def checkExistStudent(self,code: str):
        return self.__stDAL.checkExistStudent(code)