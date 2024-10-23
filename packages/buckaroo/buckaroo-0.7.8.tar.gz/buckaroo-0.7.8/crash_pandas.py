import pandas as pd
import numpy as np
bad_df = pd.DataFrame({'column': { 'foo':8, 'bad_val': np.datetime64('2005-02-25')}})
bad_df.to_json(orient='table')

#import buckaroo
#import fastf1
#ev2020 = fastf1.get_event_schedule(2020)
#small_df = ev2020[ev2020.columns[4:5]][:1]
#print(small_df)
#print("="*80)
#print(small_df.dtypes)
#print(small_df.to_json())
df = pd.read_json("""{"EventDate":{"0":1582243200000}}""")
ab = df['EventDate'].apply(pd.to_datetime)
df2= pd.DataFrame({'EventDate': ab.astype('object')})
df2.to_json(orient='table')

print(df2['EventDate'].mode())
#bad_df = pd.DataFrame({'column': {'foo': 8,'mode': df2['EventDate'].mode()}})
#bad_df = pd.DataFrame({'column': {'foo': 8, 'mode': ab.mode(), 'value_counts':ab.value_counts()}})
#bad_df = pd.DataFrame({'column': { 'foo':8, 'mode': np.datetime64('2005-02-25'), 'value_counts':ab.value_counts()}})
bad_df = pd.DataFrame({'column': { 'foo':8, 'mode': np.datetime64('2005-02-25')}})
bad_df.to_json(orient='table')

