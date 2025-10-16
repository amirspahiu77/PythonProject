# 1. Tepretaure Overview
# -find the average temperature for the entire dataset (format 2decimal points)
#
# 2.Monthly Tempreature
# - calculate the average tempature for each month
# visualize the monthly average tempetaure -> bar plot
#
# 3.Highs and Lows
# - Identify the hottest and coldest days based on temperature
#
# 4.Temperature Trends
# - creat a simple line graph showing how temperature changes over time
# -seasonal average temperature


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avg_temperature.csv')
df.columns = df.columns.str.strip()

df['Month'] = pd.to_datetime(df['Month'], format='%m-%d')


avg_temp = round(df['Temperature'].mean(), 2)
print(f"Average temperature for dataset: {avg_temp}°C")

df['Month_Num'] = df['Month'].dt.month
monthly_avg = df.groupby('Month_Num')['Temperature'].mean()

plt.figure(figsize=(8,5))
plt.bar(monthly_avg.index, monthly_avg.values, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Avg Temp (°C)')
plt.title('Monthly Average Temperature')
plt.xticks(range(1,13))
plt.show()

max_temp = df.loc[df['Temperature'].idxmax()]
min_temp = df.loc[df['Temperature'].idxmin()]

print("\n--- Highs and Lows ---")
print(f"Hottest Day: {max_temp['Month'].strftime('%m-%d')} -> {max_temp['Temperature']}°C")
print(f"Coldest Day: {min_temp['Month'].strftime('%m-%d')} -> {min_temp['Temperature']}°C")

plt.figure(figsize=(10,5))
plt.plot(df['Month'], df['Temperature'], label='Daily Temp', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%m-%d'))
plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df['Season'] = df['Month_Num'].apply(get_season)
seasonal_avg = df.groupby('Season')['Temperature'].mean()

print("\n--- Seasonal Average Temperature ---")
print(seasonal_avg)