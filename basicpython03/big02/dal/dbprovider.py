import mysql.connector

class DBProvider:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'root'
        self.db = 'big02DB'
        self.conn = None
        self.cur = None
        #khởi tạo object DBProvider sẽ tạo DB nếu chưa tồn tại
        self.__createDBIfNotExists()

    def __createDBIfNotExists(self):
        try:
            sql = f'CREATE DATABASE IF NOT EXISTS {self.db};'
            conn = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            passwd = self.password)
            cur = conn.cursor()
            cur.execute(sql)
        except Exception as error:
            print(error)
        finally:
            conn.close()
    # kết nối tới mysql database
    def connect(self):
        self.conn = mysql.connector.connect(host=self.host,
                                            user=self.user,
                                            password=self.password,
                                            db=self.db)

        self.cur = self.conn.cursor()

    #ngắt kết nối tới Database
    def close(self):
        #nếu đang kết nối thì mới đóng kết nối
        if self.conn is not None and self.cur is not None:
            self.conn.close()
            self.conn = None
            self.cur = None

    # thực thi các câu lệnh sql ở dạng chỉnh sửa dữ liệu:insert/update/delete
    def exec(self,sql,*params):
        rowCount = 0
        # Exception1, Exception2
        # Nếu exception thì in ra lỗi => có thể gộp chung để bắt Exception
        # Nếu xảy ra Exception1 thì thực hiện việc A, còn nếu xảy ra Exception2 thì thực hiện việc B
        try:
            self.connect()
            self.cur.execute(sql,*params)
            self.conn.commit()
            rowCount = self.cur.rowcount
        except Exception as err:
            print(err)
        finally:
            self.close()
        return rowCount

    # thực thi câu lệnh SQL ở dạng truy vấn dữ liệu:SELECT
    #truy vấn nhiều bản ghi
    def get(self,sql:str,*params):
        res = None
        try:
            self.connect()
            self.cur.execute(sql,*params)
            res = [row for row in self.cur.fetchall()]
        except Exception as error:
            print(error)
        finally:
            self.close()
        return res
    #truy vấn 1 bản ghi
    def getOne(self,sql:str,*params):
        res = None
        try:
            self.connect()
            self.cur.execute(sql,*params)
            res = self.cur.fetchone()
        except Exception as error:
            print(error)
        finally:
            self.close()
        return res

