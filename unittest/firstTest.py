import unittest
#from geometry import Point

class MathTest(unittest.TestCase):
    #def setUp(self):
        #print('>> setup')

    def test_addition(self):
        ans = 5+5
        self.assertEqual(10, ans)

    def test_subtraction(self):
        ans = 10-2
        self.assertEqual(8, ans)
    
    def test_multiplication(self):
        ans = 3*4
        self.assertEqual(12, ans)

    def test_division(self):
        ans = 12/4
        self.assertEqual(3, ans)
    
    def test_modulus(self):
        ans = 12 % 5
        self.assertEqual(2, ans)


if __name__ == '__main__':
    unittest.main()

