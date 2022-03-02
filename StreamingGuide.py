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

# movie objects
movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)


stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)
# display the catalog
print("Streaming Service: "+stream_serv_1.get_name()+"\nCatalog:")
catalogList = stream_serv_1.get_catalog()
for m in catalogList:
    print(m)

# create a second streaming service
stream_serv_2 = StreamingService('Hula')

stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)

print("\nStreaming Service: "+stream_serv_2.get_name()+"\nCatalog:")
catalogList = stream_serv_2.get_catalog()
for m in catalogList:
    print(m)
# delete a movie
stream_serv_2.delete_movie('The Seventh Seal')
print("\nAfter deleting 'The Seventh Seal', "+stream_serv_2.get_name()+"'s catalog - ")
catalogList = stream_serv_2.get_catalog()
for m in catalogList:
    print(m)
# add another movie
stream_serv_2.add_movie(movie_2)
print("\nAfter adding 'Home Alone', "+stream_serv_2.get_name()+"'s catalog - ")
catalogList = stream_serv_2.get_catalog()
for m in catalogList:
    print(m)

# Third streaming service
stream_serv_3 = StreamingService('Dizzy+')

stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

print("\nStreaming Service: "+stream_serv_3.get_name()+"\nCatalog:")
catalogList = stream_serv_3.get_catalog()
for m in catalogList:
    print(m)

# guide
stream_guide = StreamingGuide()
# add the three streaming services to it
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
# delete a streaming service
stream_guide.delete_streaming_service('Hula')


search_results = stream_guide.where_to_watch('Little Women')
print("\nStreaming services that shows 'Little Women'")
print(search_results)