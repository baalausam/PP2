#1. Function to check if a movie's IMDB score is above 5.5:
def is_imdb_above_5_5(movie):
    return movie['imdb'] > 5.5
#2. Function that returns a sublist of movies with an IMDB score above 5.5:
def filter_movies_above_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]
#3. Function that takes a category name and returns just those movies under that category:
def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'].lower() == category.lower()]
#4. Function that computes the average IMDB score for a list of movies:
def average_imdb_score(movies):
    if len(movies) == 0:
        return 0  # to avoid division by zero if the list is empty
    total_imdb = sum(movie['imdb'] for movie in movies)
    return total_imdb / len(movies)
#5. Function that takes a category and computes the average IMDB score of movies in that category:
def average_imdb_score_by_category(movies, category):
    filtered_movies = get_movies_by_category(movies, category)
    return average_imdb_score(filtered_movies)


'''movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Example usage:

# Check if a movie's IMDB score is above 5.5
movie = movies[0]
print(is_imdb_above_5_5(movie))  # True

# Get movies with an IMDB score above 5.5
filtered_movies = filter_movies_above_5_5(movies)
print(filtered_movies)  # List of movies with IMDB score > 5.5

# Get movies by category (e.g., Romance)
romance_movies = get_movies_by_category(movies, "Romance")
print(romance_movies)  # List of Romance movies

# Calculate average IMDB score for all movies
average_score = average_imdb_score(movies)
print(average_score)  # Average IMDB score for all movies

# Calculate average IMDB score for a specific category (e.g., Romance)
average_score_romance = average_imdb_score_by_category(movies, "Romance")
print(average_score_romance)  # Average IMDB score for Romance category'''
