import unittest
# B1
# class Calc:
#     def sum(self,arg):
#         total = 0
#         for val in arg:
#             total += val
#         return total

# class TestCalc(unittest.TestCase):
#     def setUp(self):
#         self.calc = Calc()

#     def testSumCorrect(self):
#         # Arrange
#         t1 = [0,1,2,3]
#         expectedResult = 6

#         # Act
#         actualResult = self.calc.sum(t1)

#         # Assert
#         self.assertEqual(expectedResult, actualResult)

#     def testSumIncorrect(self):
#         t1 = [0,1,2,3]
#         expectedResult =5
#         actualResult = self.calc.sum(t1)
#         self.assertNotEqual(expectedResult, actualResult)

#     def testSumRaiseTypeError(self):
#         t2 = [2,'a']
#         with self.assertRaises(TypeError):
#             actualResult = self.calc.sum(t2)

#     def teardown(self):
#         pass

# B2
class Util:
    def upper_case(self,text):
        return text.upper()

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.util = Util()
    def testUpperCaseCorrect(self):
        text = 'cumingg'
        expectedResult = 'CUMINGG'
        actualResult = self.util.upper_case(text)
        self.assertEqual(expectedResult, actualResult)
    
    def testUpperCaseInCorrect(self):
        text = 'cumingg'
        expectedResult = 'CuMINGG'
        actualResult = self.util.upper_case(text)
        self.assertNotEqual(expectedResult, actualResult)

    def testUpperCaseRaisesAttributeError(self):
        s2 = 3
        with self.assertRaises(AttributeError):
            actualResult = self.util.upper_case(s2)
    
    def teardown(self):
        pass