import pandas
from pandas import DataFrame

# from my_mod import enlarge
# another way to import if working outside of my_lambdata (most often the case)
from my_lambdata.my_mod import enlarge

print('Hello')

df = DataFrame({'a':[1,2,3], 'b':[4,5,6]})
print(df.head())