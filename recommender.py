# recommender.py

def recommend_by_genre(movies, genre):
    recommendations = []

    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            recommendations.append(movie)

    return recommendations


def recommend_by_rating(movies, min_rating):
    recommendations = []

    for movie in movies:
        if movie["rating"] >= min_rating:
            recommendations.append(movie)

    return recommendations