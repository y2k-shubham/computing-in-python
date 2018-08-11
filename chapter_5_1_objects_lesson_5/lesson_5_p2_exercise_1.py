#We've given you a class called "Song" that represents
#some basic information about a song. We also wrote a
#class called "Artist" which contains some basic
#information about an artist.
#
#Your job is to create three instances of the song class,
#called song_1, song_2, and song_3.
#
#song_1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2008
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_2 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_3 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2016
#   artist.name = "LIGHTS"
#   artist.label = "Warner Bros. Records Inc."
#
#Notice, though, that song_1 and song_2 have the same
#artist and label. That means they should each have the
#SAME instance of artist: do not create separate instances
#of artist for each song.
#
#When your code is done running, there should exist three
#variables: song_1, song_2, and song_3, according to the
#requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label
    def __repr__(self):
        repr = """
            Name  : {}
            Label : {}
        """.format(self.name, self.label)
        return repr

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
    def __repr__(self):
        repr = """
            Name   : {}
            Album  : {}
            Year   : {}
            Artist :-{}
        """.format(self.name, self.album, self.year, self.artist)
        return repr

#Write your code here!
artist_taylor_swift_big_machine = Artist(name="Taylor Swift", label="Big Machine Records, LLC")
artist_lights_warner_bros = Artist(name="LIGHTS", label="Warner Bros. Records Inc.")

song_1 = Song(
    name="You Belong With Me",
    album="Fearless",
    year=2008,
    artist=artist_taylor_swift_big_machine)

song_2 = Song(
    name="All Too Well",
    album="Red",
    year=2012,
    artist=artist_taylor_swift_big_machine)

song_3 = Song(
    name="Up We Go",
    album="Midnight Machines",
    year=2016,
    artist=artist_lights_warner_bros)

#Feel free to add code to test your code below.

print(song_1)
print(song_2)
print(song_3)
