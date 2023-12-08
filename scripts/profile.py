from ydata_profiling import ProfileReport
import pandas as pd
import os 

# convert to csv
file_path = 'data/car.data'
df = pd.read_csv(file_path, delimiter=',', header=None)
output_path = 'data/cardata.csv'
column_headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'condition']

# Assign the column names to the DataFrame
df.columns = column_headers
df.to_csv(output_path, index=False)
df = pd.read_csv('data/cardata.csv')

if not os.path.exists("profiling"):
    os.makedirs("profiling")

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/profiling.html")