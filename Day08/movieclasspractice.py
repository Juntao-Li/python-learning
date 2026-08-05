class Movie:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"Id:{self.id} | Name:{self.name} | Rating:{self.rating}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.rating < other.rating

if __name__ == "__main__":
    movie1 = Movie("001", "Interstellar", 9.5)
    movie2 = Movie("002", "Inception", 9.2)
    movie3 = Movie("001", "Interstellar (Copy)", 8.8)
    movie4 = Movie("003", "Avatar", 8.5)

    print(movie1)
    print()

    movies = [movie1, movie2, movie4]
    print(movies)
    print()

    print(movie1 == movie3)
    print(movie1 == movie2)
    print()

    movies.sort()

    for movie in movies:
        print(movie)
