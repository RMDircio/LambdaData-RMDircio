import unittest

def calc_area(l, w):
    '''
    Paramaters:
    l and w are real positive numbers.
    Representing the length and width of a rectangle.
    '''
    if l <= 0 or  w <= 0:
        raise ValueError

    return l * w

class TestCalculations(unittest.TestCase):
    
    def test_calc_area(self):
        self.assertEqual(calc_area(5,3), 15)

        with self.assertRaises(ValueError):
            calc_area(-5,3)
        
        with self.assertRaises(ValueError):
            calc_area(5,-3)

if __name__ == "__main__":
    unittest.main()