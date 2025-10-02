import pandas as pd
from pandas.core.algorithms import duplicated

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

first_row = df.head()
print(first_row)

country_data = df['Country']
print(country_data)

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ']>100]
print(filtered_df)

#Handling Missing and Duplicate Data
null_mask = df.insull()
null_count = null_mask.sum()
print("\nCount of null values in each column:")
print(null_count)

df.dropna(implace=True)
print("\nDataset information after removing null vvalues: ")
print(df.info())

duplicated_count = df.duplicated().sum()
print("\nCount of duplicated rows:")
print(duplicated_count)

df.drop_duplicates(keep='first', inplace=True)
#df.drop_duplicates(keep='first', implace=True)

average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)

sorted_average_iq_per_continent = average_iq_per_continent.sort_values(ascending=False)
print(sorted_average_iq_per_continent)













