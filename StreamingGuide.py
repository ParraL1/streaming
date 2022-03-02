#Name: Lilliana Parra
#Date: 03/02/2022
#Github user: ParraL1
#Description: Movie streaming service

# class for movies
class Movie:
    # constructor
    def __init__(self, title, genre, director, year):
        # movie's title, genre, director and year
        # parameters
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    # movie's title
    def get_title(self):
        return self._title

    # movie's genre
    def get_genre(self):
        return self._genre

    # movie's director
    def get_director(self):
        return self._director

    # movie's year
    def get_year(self):
        return self._year

# StreamingService
class StreamingService:
    # constructor
    def __init__(self, name):
        self._name = name
        self._catalog = []

    # streaming service's name
    def get_name(self):
        return self._name

    # streaming service's catalog
    def get_catalog(self):
        return self._catalog

    # adding a movie to streaming service catalog
    def add_movie(self, movie):
        self._catalog.append(movie)

    # deleting a movie from streaming service catalog
    def delete_movie(self, movieTitle):
        # loop
        for m in self._catalog:

            if m.get_title() == movieTitle:

                self._catalog.remove(m)

# StreamingGuide
class StreamingGuide:
    # constructor
    def __init__(self):

        self._services = []

    # add object to streaming service
    def add_streaming_service(self, service):
        self._services.append(service)

    # delete object from streaming service
    def delete_streaming_service(self, serviceName):

        for s in self._services:

            if s.get_name() == serviceName:

                self._services.remove(s)

    # returns list of streaming services
    def where_to_watch(self, title):

        result = []
        found = False


        for i in range(len(self._services)):

            catalog = self._services[i].get_catalog()
            for movie in catalog:
                if movie.get_title() == title:
                    if found == False:
                        r1 = title + "("+str(movie.get_year())+")"
                        result.append(r1)
                        found = True
                    result.append(self._services[i].get_name())


        if found == True:
            return result
        else:
            return None

# movie objects
movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)
