# main.py

from movies import load_movies, display_movies
from recommender import recommend_by_genre, recommend_by_rating

FILE_PATH = "data/movies.txt"

movies = load_movies(FILE_PATH)

while True:
    print("\n===== MOVIE RECOMMENDATION SYSTEM =====")
    print("1. Show all m1ovies")
    print("2. Recommend by genre")
    print("3. Recommend by rating")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_movies(movies)

    elif choice == "2":
        genre = input("Enter genre (Action, Romance, Sci-Fi, Drama): ")
        results = recommend_by_genre(movies, genre)

        print("\nRecommendations:")
        for m in results:
            print(f"{m['title']} | {m['rating']}")

    elif choice == "3":
        rating = float(input("Enter minimum rating: "))
        results = recommend_by_rating(movies, rating)

        print("\nTop Rated Movies:")
        for m in results:
            print(f"{m['title']} | {m['genre']} |  {m['rating']}")

    elif choice == "4":
        print("Goodbye ")
        break

    else:
        print("Invalid choice!")