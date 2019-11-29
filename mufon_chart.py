from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("ENV/mufon.csv")

freq_xax = df["Date_Submitted"].unique()[::-1]

freq_yax = df["Date_Submitted"].value_counts().sort_index()

day_xax = df["Day_Submitted"].value_counts()[::-1]

plt.plot(freq_yax, color="green", linestyle="solid")
plt.title("Daily Frequency")
plt.ylabel("Number Of Sightings")
plt.xticks(rotation=90)

fig, ax = plt.subplots()
# plt.title("Daily Frequency")
# plt.ylabel("Number Of Sightings")
# freq_yax.plot(ax=ax, kind='bar')

plt.title("Day Density")
plt.ylabel("Number Of Sightings")
day_xax.plot(ax=ax, kind='bar')

plt.show()
