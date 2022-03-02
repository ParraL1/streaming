#Name: Lilliana Parra
#Date: 03/02/2022
#Github user: ParraL1
#Description: Movie streaming service

# a class named Movie
class Movie:
    # constructor
    def __init__(self, title, genre, director, year):
        # movie's title, genre, director and year

        self._title = title
        self._genre = genre
        self._director = director
        self._year = year
    # title
    def get_title(self):
        return self._title
    # genre
    def get_genre(self):
        return self._genre
    # director
    def get_director(self):
        return self._director
    # movie year
    def get_year(self):
        return self._year
    def __str__(self):
        return self._title+"("+str(self._year)+"), Director: "+self._director+", Genre: "+self._genre
# Streaming Service
class StreamingService:
    # constructor
    def __init__(self, name):
        # streaming service's name to the given parameter
        self._name = name
        # start catalog to an empty list
        self._catalog = []
    # streaming service name
    def get_name(self):
        return self._name
    # catalog
    def get_catalog(self):
        return self._catalog
    # to add a movie to catalog
    def add_movie(self, movie):
        self._catalog.append(movie)
    # delete a movie from the catalog
    def delete_movie(self, movieTitle):
        # loop
        for m in self._catalog:
            if m.get_title() == movieTitle:
                self._catalog.remove(m)
class StreamingGuide:
    # constructor
    def __init__(self):
        # service's list to an empty list
        self._services = []
    def add_streaming_service(self, service):
        self._services.append(service)
    def delete_streaming_service(self, serviceName):
        # loop
        for s in self._services:
            if s.get_name() == serviceName:
                self._services.remove(s)
    # returns the list
    def where_to_watch(self, title):
        # empty result list
        result = []
        found = False
        # loop
        for i in range(len(self._services)):
            catalog = self._services[i].get_catalog()
            for movie in catalog:
                if movie.get_title() == title:
                    if found == False:
                        # create a string with the movie name + year
                        r1 = title + "("+str(movie.get_year())+")"
                        result.append(r1)
                        found = True
                    result.append(self._services[i].get_name())
        # return the list
        if found == True:
            return result
        # return None
        else:
            return None
