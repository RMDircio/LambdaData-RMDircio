# LambdaData-RMDircio

## Installation

pip install -i https://test.pypi.org/simple/ my-lamb-data-pt5

## Usage

Adds a column of US state names to a corresponding column of US state abbreviations.
    
Parameters:
    my_df (pandas.DataFrame) has a column called 'abbrev' with US state abbreviations.
    
Returns:
    Copy of the original dataframe, with another column.

from my_lamb_data.my_mod import enlarge

x = 11
print(enlarge(x))
MY_MOD

def enlarge(n):
    return n * 100