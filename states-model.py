import statsmodels.api as sm
import pandas as pd
from patsy import dmatrices

data = sm.datasets.get_rdataset("Guerry", "HistData").data
var_list = ['department', 'lottery', 'literacy', 'wealth', 'region']
df = data[var_list]
df = df[-5:]
