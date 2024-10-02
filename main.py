"""
Top 100 movies

Author: Alan
Date: October 2nd 2024

This script gets a list of the best movies of all the time using web scrapping from the EmpireOnline.com
https://www.empireonline.com/movies/features/best-movies-2/
"""

from requests import get
from bs4 import BeautifulSoup
import lxml

def get_movie_list():
    """
    Using requests library, gets a list of movies finding the element that coincides with the search.
    In the EmpireOnline.com list, all the movies names are in the h3 heading element, and they are using the listicleItem_listicle-item__title__BfenH class.
    Then we convert the data into a list of Strings
    :return: List of Strings that contain the list of movies of the website from last to first order
    """

    # Get the file data of the link with the best movies of all the time
    response = get(url="https://www.empireonline.com/movies/features/best-movies-2/")

    # Store the data as text
    web_page = response.text

    # New BeautifulSoup object
    soup = BeautifulSoup(web_page, "lxml")

    # Get all the movies of the h3 heading tag and the correct class (it was updated)
    all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

    # Make a list using the all_movies list that will convert our data into text (specifically the text data)
    movie_list = [movie.getText() for movie in all_movies]

    # Order from the first to the last
    # [start:finish:count]
    return movie_list[::-1]

def create_file(movie_list):
    """
    Creates a new text file with a list of the movies
    :param movie_list: List of Strings with the list of the movies
    :return:
    """

    # Create a new file called movies.txt with the data of
    with open(file="movies.txt", mode="w") as file:
        # For each movie in the movies list will be written in the movies.txt file
        for movie in movie_list:
            # Add "\n" to add a new line once we write a movie
            file.write(f"{movie}\n")

# Get a list of movies
movies = get_movie_list()

# Create a txt file for movies
create_file(movies)
