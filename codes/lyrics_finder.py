import lyricsgenius
genius = lyricsgenius.Genius('Your Genius Public API')

songname = genius.search_song("the world's continuation romanized")
print(songname.lyrics)

# artist = genius.search_artist("Queen", max_songs=3)
# print(artist.songs)

# song = artist.song("Bohemian Rhapsody")
# print(song.lyrics)