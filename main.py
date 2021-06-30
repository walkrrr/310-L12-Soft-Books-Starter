import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

print(data["language_code"])

sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", sizes=(20, 180), data=data)

plt.xlabel("Average Rating")
plt.ylabel("Number of Pages")
plt.title("Books and Book Ratings on Goodreads")
plt.savefig("books_and_bookratings.png")



