#!/bin/python3

import math
import os
import random
import re
import sys

import requests
import json

# https://jsonmock.hackerrank.com/api/movies?Year=2000&page=1&per_page=100
#
# Complete the 'getMovies' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER year
#  2. STRING query
#

def getMovies(year, query):
    # Write your code here
    # query = query.replace("*", "")
    # query = query.replace("*", "\w")
    pageNumber = 1
    url = f"https://jsonmock.hackerrank.com/api/movies?Year={year}&page={pageNumber}"
    url_2 = f"https://jsonmock.hackerrank.com/api/movies?Year={year}&page=2"
    print(url)
    print(url_2)
    movie_titles = []
    movie_row = []
    movie_array = []
    all_data = requests.get(url)
    all_data_2 = requests.get(url_2)
    data = all_data.json()
    data_2 = all_data_2.json()
    data = data['data']
    data_2 = data_2['data']
    data = data + data_2
    ctr = 0
    for idx, movie in enumerate(data):
        if query.endswith("*"):
            clean_query = query.replace("*", "")
            if re.search(query, movie['Title'].lower()):
                if movie['Title'].lower().startswith(clean_query):
                    # movie_titles.append(movie['Title'])
                    # movie_row[0] = movie['imdbID']
                    # movie_row[1] = movie['Title']
                    # movie_row.append(movie['imdbID'])
                    # movie_row.append(movie['Title'])
                    movie_row = [movie['imdbID'], movie['Title']]
                    ctr += 1
                    movie_array.append(movie_row)
        elif query.startswith("*"):
            clean_query = query.replace("*", "")
            if re.search(query, movie['Title'].lower()):
                if movie['Title'].lower().endswith(clean_query):
                    movie_row = [movie['imdbID'], movie['Title']]
                    movie_array.append(movie_row)
        elif query.startswith("*") and query.endswith("*"):
            if re.search(query, movie['Title'].lower()):
                movie_row = [movie['imdbID'], movie['Title']]
                movie_array.append(movie_row)
        else:
            if re.search(query, movie['Title'].lower()):
                movie_row = [movie['imdbID'], movie['Title']]
                movie_array.append(movie_row)

    # print(data.json())
    print(data)
    # print(movie_titles)
    print(movie_array)
    # return data.json()
    return movie_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    query = input()

    result = getMovies(year, query)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
