import pandas as pd

data = {'Name':['Alice','Bob','Charlie'],
        'Age':[25, 30, 22],
        'City': ['Pristine', 'New York', 'LA']}

df = pd.DataFrame(data)
print(df)

#Reading and Writing Data

#Read data from a CSV File
df = pd.read_csv('your_dataset.csv')

#Write data to CSV File
df.to_csv('output_dataset.csv', index=False)