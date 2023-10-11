import statsmodels.api as sm
import pandas as pd
from patsy import dmatrices

# Load Guerry dataset and check column names
data = sm.datasets.get_rdataset("Guerry", "HistData").data
print(data.columns)

# Select variables and check column names
var_list = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = data[var_list]
print(df.columns)

# Select last five rows of data
df = df[-5:]

# Create design matrices for linear regression
y, X = dmatrices('Literacy ~ Lottery + Wealth + Region', data=df, return_type='dataframe')

# Fit linear regression model
model = sm.OLS(y, X).fit()

# Print model summary
print(model.summary())
