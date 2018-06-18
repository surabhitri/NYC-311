from __future__ import print_function
import pandas as pd

fname_data = '311-service-requests.csv'
df_311_calls = pd.read_csv(fname_data)
print( df_311_calls['Complaint Type'].value_counts()[:5])
