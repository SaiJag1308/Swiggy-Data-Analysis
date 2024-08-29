import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import colorbar
import random as rd

# Check for correct data
dataframe = pd.read_csv("Swiggy data.csv")
# print(dataframe.head())
'''
amb_rating = np.zeros((148,1))
for i in range(0,148):
    amb_rating[i] = round(rd.uniform(0,5),1)
# print(amb_rating)

dataframe.insert(7,"ambience rating",amb_rating,True)
print(dataframe)
'''
# Converting rate column to float data type
def handleRate(value):
	value=str(value).split('/')
	value=value[0]
	return float(value)

dataframe['food rating']=dataframe['food rating'].apply(handleRate)
print(dataframe.head())

# Summary of the data(to check for null data)
dataframe.info()

# Plotting the count of each type of hotels
sns.countplot(x=dataframe['listed_in(type)'],palette="Set1")
plt.xlabel("Type of hotel")
plt.show()

# Plotting Hotels preferred vs Votes
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="black", marker="o")
plt.xlabel("Type of hotel", c="black", size=20)
plt.ylabel("Votes", c="black", size=20)
plt.show()

# Hotel with maximum and minimum votes
max_votes = dataframe['votes'].max()
hotel_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print("Hotel(s) with the maximum votes:")
print(hotel_with_max_votes)

min_votes = dataframe['votes'].min()
hotel_with_min_votes = dataframe.loc[dataframe['votes'] == min_votes, 'name']
print("Hotel(s) with the minimum votes:")
print(hotel_with_min_votes)

# Hotels accepting online orders or not
sns.countplot(x=dataframe['online_order'])
plt.xlabel("online order")
plt.ylabel("count")
plt.show()

# Plot for food rating
plt.hist(dataframe['food rating'],bins=10)
plt.title("Food Ratings Distribution")
plt.show()

# Approximate cost for two people
couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

# Hotels which books tables
sns.countplot(x=dataframe['book_table'])
plt.show()

# Plot for ambience rating
plt.hist(dataframe["ambience rating"],bins=20)
plt.title("Ambience Ratings Distribution")
plt.show()