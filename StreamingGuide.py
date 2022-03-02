#Name: Lilliana Parra
#Date: 03/02/2022
#Github user: ParraL1
#Description: Movie streaming service

# Movie Class
class Movie:
    def __init__(self, title, genre, director, year):

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


    def __str__(self):
        return self._title + "(" +str (self._year) +"), Director: "+self._director+", Genre: "+self._genre

# StreamingService
class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = []

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie):
        self._catalog.append(movie)

    def delete_movie(self, movieTitle):
        for movie in self._catalog:
            if movie.get_title() == movieTitle:
                self._catalog.remove(movie)


class StreamingGuide:
    def __init__(self):
        self._services = []

    def add_streaming_service(self, service):
        self._services.append(service)

    def delete_streaming_service(self, serviceName):
        for service in self._services:
            if service.get_name() == serviceName:
                self._services.remove(service)

    def where_to_watch(self, title):
        result = []
        found = False

        for i in range(len(self._services)):
            catalog = self._services[i].get_catalog()
            for movie in catalog:
                if movie.get_title() == title:
                    if found == False:
                        desired_movie = title + "("+ str (movie.get_year ( )) +")"
                        result.append(desired_movie)
                        found = True
                    result.append(self._services[i].get_name())

        if found == True:
            return result
        else:
            return None