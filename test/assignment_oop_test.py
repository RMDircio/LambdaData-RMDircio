
import unittest
from pandas import DataFrame
from my_lamb_data.assignment_oop import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def test_add_state_names_oop(self):
        
        state_df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        processor = DataProcessor(state_df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        
        processor.add_state_names()

        self.assertEqual(list(processor.df.columns), ['abbrev', 'name'])
        self.assertEqual(processor.df.iloc[0]['abbrev'], 'CA')
        self.assertEqual(processor.df.iloc[0]['name'], 'California')



if __name__ == '__main__':
    unittest.main()

# python -m test.assignment_oop_test
