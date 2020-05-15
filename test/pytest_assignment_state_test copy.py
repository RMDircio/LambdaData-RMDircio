
from pandas import DataFrame
from my_lamb_data.assignment_state import add_state_names




def test_add_state_names():
        
    state_df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    # self.assertEqual(list(state_df.columns), ['abbrev'])
    assert list(state_df.columns) == ['abbrev']

    result = add_state_names(state_df)
    # self.assertEqual(list(result.columns), ['abbrev', 'name'])
    # self.assertEqual(result.iloc[0]['abbrev'], 'CA')
    # self.assertEqual(result.iloc[0]['name'], 'California')
    assert list(result.columns) == ['abbrev', 'name']
    assert result.iloc[0]['abbrev'] == 'CA'
    assert result.iloc[0]['name'] == 'California'



# python -m test.assignment_state_test