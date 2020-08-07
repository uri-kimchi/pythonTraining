import unittest
import ToBeTested

class MyAutoTest ( unittest.TestCase):
    def testUpper(self):
        x = 'Uri Kimchi was here'
        expectedResult = 'URI KIMCHI WAxS HERE'
        result = ToBeTested.tUpper(x)
        self.assertEqual(result,expectedResult)

    def testLower(self):
        x = 'Uri Kimchi was here'
        expectedResult = 'uri kimchi was here'
        result = ToBeTested.tLower(x)
        self.assertEqual(result,expectedResult)

if __name__ == "__main__" :
    unittest.main()
