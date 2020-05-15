import unittest
from pandas import DataFrame
from my_lamb_data.assignment_state import add_state_names


class TestAssignment(unittest.TestCase):

    def test_add_state_names(self):
        
        state_df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        self.assertEqual(list(state_df.columns), ['abbrev'])

        result = add_state_names(state_df)
        self.assertEqual(list(result.columns), ['abbrev', 'name'])
        self.assertEqual(result.iloc[0]['abbrev', 'CA'])
        self.assertEqual(result.iloc[0]['name', 'California'])



if __name__ == '__main__':
    unittest.main()

# python -m test.assignment_state_test