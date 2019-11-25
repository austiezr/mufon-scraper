from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("ENV/mufon.csv")

yax = df["Date_Submitted"].unique()[::-1]

xax = df["Date_Submitted"].value_counts().sort_index()

plt.plot(xax, color="green", linestyle="solid")
plt.title("Daily Frequency")
plt.ylabel("Number Of Sightings")

fig, ax = plt.subplots()
plt.title("Daily Frequency")
plt.ylabel("Number Of Sightings")
xax.plot(ax=ax, kind='bar')

plt.show()
