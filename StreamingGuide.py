#Name: Lilliana Parra
#Date: 03/02/2022
#Github user: ParraL1
#Description: Movie streaming service

def __init__(self,title,genre,director,year):
    self._title=title
    self._genre=genre
    self._director=director
    self._year=year
  def get_title(self):
    return self._title
  def get_genre(self):
    return self._genre
  def get_director(self):
    return self._director
  def get_year(self):
    return self._year

class StreamingService:
  def __init__(self,name):
    self.name=name
    self.catalog=dict()
  def get_name(self):
    return self.name
  def get_catalog(self):
    return self.catalog
  def add_movie(self,movie):
    movietitle=movie.get_title()
    self.catalog[movietitle]=movie
  def delete_movie(self,title):
    if title in self.catalog.keys():
      del self.catalog[title]

class StreamingGuide:
  def __init__(self):
    self._data=[]
  def add_streaming_service(self,streamingservice):
    self._data.append(streamingservice)
  def delete_streaming_service(self,name):
    for i in self._data:
      if(i.get_name()==name):
        self._data.remove(i)
        break
  def where_to_watch(self,title):
    l=[]
    for i in self._data:
      cata=i.get_catalog()
      if title in cata.keys():
        mobj=cata[title]
    ye=mobj.get_year()
    s1=str(title)+ "(" + str(ye) + ")"
    l.append(s1)
    if len(self._data)==0:
      l.append("None")
    else:
      for a in self._data:
        cat=a.get_catalog()
        if title in cat.keys():
          l.append(a.get_name())
    return l