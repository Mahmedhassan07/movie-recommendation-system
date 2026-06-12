# movies.py

def load_movies(filename):
    movies = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            movie = {
                "id": parts[0],
                "title": parts[1],
                "genre": parts[2],
                "rating": float(parts[3])
            }
            movies.append(movie)
    return movies


def display_movies(movies):
    print("\nAvailable Movies:")
    for m in movies:
        print(f"{m['id']}. {m['title']} | {m['genre']} | {m['rating']}")