import pandas as pd
data = [['John', 25, 'colachal'],
       ['benny', 30, 'London'],
       ['libin', 35, 'Paris']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print(df)
