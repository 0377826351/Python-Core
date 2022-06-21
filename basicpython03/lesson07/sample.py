import unittest

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Point(x, y)


class PointTestAdd(unittest.TestCase):
    # phần 1: setup(chuẩn bị dữ liệu, tài nguyên, điều kiện để thực hiện các test case)
    # luôn chạy đầu tiên
    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, 2)

    # phần 2: các testcase (test xem hàm hamCanTesst có hoạt động đúng không)
    def testAddCorrect(self):
        # phần 1: Arrange(chuẩn bị dữ liệu, điều kiện nhưng chỉ trong hàm này)
        expectedResult = Point(4, 6)
        # phần 2:Act (thực thi hành động cần test)
        actualResult = self.p1 +self.p2
        # phần 3:Assert(Kiểm tra, thông báo kết quả thực thi testcase này: pass/fail)
        self.assertEqual(expectedResult.x, actualResult.x)
        self.assertEqual(expectedResult.y, actualResult.y)

        #teardown optional
    #các testcase (test xem hàm hamCanTesst có hoạt động sai không)
    def testAddInCorrect(self):
        # phần 1: Arrange(chuẩn bị dữ liệu, điều kiện nhưng chỉ trong hàm này)
        expectedResult = Point(2, 2)
        # phần 2:Act (thực thi hành động cần test)
        actualResult = self.p1 +self.p2
        # phần 3:Assert(Kiểm tra, thông báo kết quả thực thi testcase này: pass/fail)
        self.assertNotEqual(expectedResult.x, actualResult.x)
        self.assertNotEqual(expectedResult.y, actualResult.y)

    def testAddRaiseTypeError(self):
        # phần 1: Arrange(chuẩn bị dữ liệu, điều kiện nhưng chỉ trong hàm này)
        p3 = Point('a', 2)
        # phần 2:Act (thực thi hành động cần test)
        with self.assertRaises(TypeError):
            actualResult = self.p1 +p3

        
    # phần 3: teardown(dọn dẹp, khôi phục trạng thái ban đầu sau khi chạy test xong)
    # luôn chạy cuối cùng
    def teardown(self):
        pass


    #TODO Test cho  hàm __truediv__ method
    #correct,incorrect,typeerror,ZeroDivisionError
class PointTestDiv(unittest.TestCase):
    # phần 1: setup(chuẩn bị dữ liệu, tài nguyên, điều kiện để thực hiện các test case)
    # luôn chạy đầu tiên
    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, 2)

    # phần 2: các testcase (test xem hàm hamCanTesst có hoạt động đúng không)
    def testDivCorrect(self):
        # phần 1: Arrange(chuẩn bị dữ liệu, điều kiện nhưng chỉ trong hàm này)
        expectedResult = Point(3, 2)
        # phần 2:Act (thực thi hành động cần test)
        actualResult = self.p1 / self.p2
        # phần 3:Assert(Kiểm tra, thông báo kết quả thực thi testcase này: pass/fail)
        self.assertEqual(expectedResult.x, actualResult.x)
        self.assertEqual(expectedResult.y, actualResult.y)

        #teardown optional
    #các testcase (test xem hàm hamCanTesst có hoạt động sai không)
    def testDivInCorrect(self):
        # phần 1: Arrange(chuẩn bị dữ liệu, điều kiện nhưng chỉ trong hàm này)
        expectedResult = Point(2, 2)
        # phần 2:Act (thực thi hành động cần test)
        actualResult = self.p1 +self.p2
        # phần 3:Assert(Kiểm tra, thông báo kết quả thực thi testcase này: pass/fail)
        self.assertNotEqual(expectedResult.x, actualResult.x)
        self.assertNotEqual(expectedResult.y, actualResult.y)

    def testDivRaiseTypeError(self):
        # phần 1: Arrange(chuẩn bị dữ liệu, điều kiện nhưng chỉ trong hàm này)
        p3 = Point('a', 2)
        # phần 2:Act (thực thi hành động cần test)
        with self.assertRaises(TypeError):
            actualResult = self.p1 / p3

    def testDivRaiseZeroDivisonError(self):
        p3 = Point(2, 2)
        with self.assertRaises(ZeroDivisionError):
            actualResult = self.p1 / p3

        
    # phần 3: teardown(dọn dẹp, khôi phục trạng thái ban đầu sau khi chạy test xong)
    # luôn chạy cuối cùng
    def teardown(self):
        pass