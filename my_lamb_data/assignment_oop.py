# ASSIGNMENT 2
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame


def add_state_names(my_df):
    '''
    Adds a column of US state names to a corresponding column of 
    US state abbreviations.
    
    Parameters:
        my_df (pandas.DataFrame) has a column called 'abbrev' with 
        US state abbreviations.
    
    Returns:
        Copy of the original dataframe, with another column.
    '''
    new_df = my_df.copy()
    names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut'}
    # breakpoint()
    new_df['name'] = new_df['abbrev'].map(names_map)
    return new_df

if __name__ == '__main__':

    state_df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    print(state_df.head())

    df_2 = add_state_names(state_df)
    print(df_2)