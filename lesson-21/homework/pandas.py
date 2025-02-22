#exercise 1

import pandas as pd
data = {
    'BusinessEntityID': [275, 275, 275, 275, 275, 275],
    'SalesYear': [2005, 2005, 2006, 2006, 2006, 2006],
    'CurrentQuota': [367000, 556000, 502000, 550000, 1429000, 1324000]
}
df = pd.DataFrame(data)
df = df.sort_values(by=['BusinessEntityID', 'SalesYear'])
df['PreviousQuota'] = df.groupby('BusinessEntityID')['CurrentQuota'].shift(1)
print(df)


#exercise 2

import pandas as pd
data = {
    'BusinessEntityID': [275, 275, 275, 275, 275, 275],
    'SalesYear': [2005, 2005, 2006, 2006, 2006, 2006],
    'CurrentQuota': [367000, 556000, 502000, 550000, 1429000, 1324000]
}
df = pd.DataFrame(data)
df = df.sort_values(by=['BusinessEntityID', 'SalesYear'])
df['NextQuota'] = df.groupby('BusinessEntityID')['CurrentQuota'].shift(-1)
print(df)

#exercise 3

import pandas as pd
data = {
    'EmpId': [1, 2, 3, 4, 5],
    'EmpName': ['Pawan', 'Zuzu', 'Parveen', 'Mahesh', 'Ramesh'],
    'BirthDate': ['04-12-1983', '28-11-1986', '07-05-1977', '13-01-1983', '09-05-1983']
}
df = pd.DataFrame(data)
df['BirthDate'] = pd.to_datetime(df['BirthDate'], format='%d-%m-%Y') & (df['BirthDate'].dt.day <= 15)]
print(filtered_df[['EmpId', 'EmpName', 'BirthDate']])

# exercise 4

import pandas as pd
data = {
    'MName': ['A', 'A', 'B', 'B', 'D', 'E'],
    'AName': ['Amitabh', 'Vinod', 'Amitabh', 'Vinod', 'Amitabh', 'Vinod'],
    'Roles': ['Actor', 'Villain', 'Actor', 'Actor', 'Actor', 'Actor']
}
df = pd.DataFrame(data)
actor_df = df[df['Roles'] == 'Actor']
result = actor_df.groupby('MName').filter(lambda x: set(['Amitabh', 'Vinod']).issubset(set(x['AName'])))
print(result)

# exercise 5


import pandas as pd
data = {
    'ID': [1, 1],
    'Name': ['P', None],
    'Typed': [None, 'Q']
}
df = pd.DataFrame(data)
cleaned_df = df.dropna()
print(cleaned_df)
