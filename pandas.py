import pandas as pd

data = pd.DataFrame({
    'x1': ['x', 'y', 'z', 'xx', 'yy', 'zz'],
    'x2': range(16, 22),
    'x3': range(1, 7),
    'x4': ['a', 'b', 'c', 'd', 'e', 'f'],
    'x5': range(30, 24, -1)
})

print(data)

s1 = pd.Series([1, 2, 3, 4, 5, 6])
s2 = pd.Series([1.5, 2.7, 3.6, 4.3, 5.1, 6.9])
s3 = pd.Series(['a', 'b', 'c', 'd','e','f'])

data = pd.DataFrame({
    'First': s1,
    'Second': s2,
    'Third': s3
})

print(data)
