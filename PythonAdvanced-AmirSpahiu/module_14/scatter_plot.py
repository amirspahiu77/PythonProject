import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avgIQpercountry.csv")

plt.figure(figsize=(10,6))

plt.scatter(df['Mean years of schooling - 2021'], df['Average IQ'], color='purple', alpha=0.7)

plt.xlabel('Scatter Plot of mean Years of schooling vs Average IQ')

plt.ylabel('Average IQ')

plt.grid(True, linestyle='--', alpha=0.7)

plt.show()