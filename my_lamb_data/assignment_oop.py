# ASSIGNMENT 3
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame

class DataProcessor():
    def __init__(self, state_df):
        '''
        Parameters:
            my_df (pandas.DataFrame) has a column called 'abbrev' with 
            US state abbreviations.
        '''
        self.df = state_df
    

    def add_state_names(self):
        '''
        Adds a column of US state names to a corresponding column of 
        US state abbreviations.
        ''''

    
        names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut'}
        # breakpoint()
        self.df['name'] = self.df['abbrev'].map(names_map)
        return self.df

if __name__ == '__main__':

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    processor = DataProcessor(df)
    print(processor.df.head())

    processor.add_state_names()
    print(processor.df.head())