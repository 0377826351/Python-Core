from dal import ScoreDAL
from dto import ScoreDTO
class ScoreBLL:
    def __init__(self):
        self.__scBLL = ScoreDAL()

    def insert(self,sc:ScoreDTO):
        return self.__scBLL.insert(sc)
    
    def update(self,sc:ScoreDTO):
        return self.__scBLL.update(sc)

    def delete(self,codeST:str,codeSB:str):
        return self.__scBLL.delete(codeST,codeSB)

    def get(self):
        return self.__scBLL.get()

    def getByCode(self,codeST: str,codeSB:str):
        return self.__scBLL.getByCode(codeST,codeSB)

    def search(self,text:str):
        return self.__scBLL.search(text)

    def checkExistScore(self,codeST: str,codeSB:str):
        return self.__scBLL.checkExistScore(codeST,codeSB)
    
    def data(self):
        return self.__scBLL.data()