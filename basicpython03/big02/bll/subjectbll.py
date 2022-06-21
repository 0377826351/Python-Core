from dal import SubjectDAL
from dto import SubjectDTO

class SubjectBLL:
    def __init__(self):
        self.__sbBLL = SubjectDAL()

    def insert(self,sb:SubjectDTO):
        return self.__sbBLL.insert(sb)

    def update(self,sb:SubjectDTO):
        return self.__sbBLL.update(sb)

    def delete(self,code:str):
        return self.__sbBLL.delete(code)

    def get(self):
        return self.__sbBLL.get()
    
    def getByCode(self,code: str):
        return self.__sbBLL.getByCode(code)

    def search(self,text:str):
        return self.__sbBLL.search(text)

    def checkExistSubject(self,code: str):
        return self.__sbBLL.checkExistSubject(code)

    def checkExistSubjectName(self,name: str):
        return self.__sbBLL.checkExistSubjectName(name)