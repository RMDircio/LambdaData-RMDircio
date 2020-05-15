# ASSIGNMENT 3
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)

from pandas import DataFrame

class MyFrame(DataFrame):

    def add_state_names(self):
        '''
        Adds a column of US state names to a corresponding column of 
        US state abbreviations.
        '''

        names_map = {'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut'}
        # breakpoint() 
        self['name'] = self['abbrev'].map(names_map)
        
if __name__ == '__main__':

    my_frame = MyFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.head())