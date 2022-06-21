class DataDTO:
    def __init__(self,codeST:str,fullName:str,birthDay:str,sex:int,address:str,phone:str,email:str,codeSB:str,processPoint:float,endPoint:float,finalGrade:float,rank:float):
        self.CodeST = codeST
        self.FullName = fullName
        self.BirthDay = birthDay
        self.Sex = sex
        self.Address = address
        self.Phone = phone
        self.Email = email
        self.CodeSB = codeSB
        self.ProcessPoint = processPoint
        self.EndPoint = endPoint
        self.FinalGrade = finalGrade
        self.Rank = rank