import pandas as pd

# print(pd.__version__)

# lst= [1,2,3,4,5]
# print(lst)

# a=pd.Series(lst)
# print(a)    
# print((a))

# empty=pd.Series()   
# print(empty)

# a=pd.Series(['a','b','c','d','e'],index=[10,20,30,40,50])
# print(a)

# b=pd.Series(['a','b','c','d','e'],index=[10,11,12,13,14])
# print(b)

# scaler_series=pd.Series(0.5,index=[1,2,3,4,5])
# print(scaler_series)

dict_series=pd.Series({'a': 0, 'b': 1, 'c': 2})
print(dict_series)

print(dict_series['a'])

print(max(dict_series))

array_series=pd.Series({'p': [1,2,3], 'q': [4,5,6], 'r': [7,8,9]})
print(array_series)