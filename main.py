#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Percy Jackson & the Olympians: The Lightning Thief"

print("My favourite movie is" , favMovie)



#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)



print("\n\n")

#Create a new variable to store a new data set with a certain genre
sfMovieBooleanList = movieData["genres"].str.contains("Science Fiction")
sfMovieData = movieData.loc[sfMovieBooleanList]

numOfMovies = sfMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Science Fiction in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Fiction")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min_rating = sfMovieData["audience_rating"].min()
fav_rating = favMovieData["audience_rating"].values[0]  
difference = fav_rating - min_rating
print("The min audience rating of the data set is: " + str(min_rating))
print(favMovie + " is rated " + str(difference) + " points higher than the lowest rated movie.")
print()

#find max
max_rating = sfMovieData["audience_rating"].max()
difference = fav_rating - max_rating
print("The max audience rating of the data set is: " + str(max_rating))
print(favMovie + " is rated " + str(difference) + " points lower than the highest rated movie.")
print()

#find mean
mean_sf = sfMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean_sf))
if fav_rating>mean_sf:
      print(favMovie + " is higher than the mean movie rating.")
elif fav_rating==mean_sf:
      print(favMovie + " is the same as the mean movie rating.")
else:
      print(favMovie + " is lower than the mean movie rating.")
print("\n\n")
#find median
median_sf = sfMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median_sf))
if fav_rating>median_sf:
      print(favMovie + " is higher than the median movie rating.")
elif fav_rating==median_sf:
      print(favMovie + " is the same as the median movie rating.")
else:
      print(favMovie + " is lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(sfMovieData["audience_rating"] , range = (0,100), bins = 20)


#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Science Fiction Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Science Fiction Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most frequent rating range for science fiction movies appears to be around 60–70"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = sfMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Ratings vs Critic Ratings for Science Fiction Movies")
plt.xlabel("Audience Ratings")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between the audience and critic ratings for science fiction movies"
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
