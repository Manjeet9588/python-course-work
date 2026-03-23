'''Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop'''

def make_album(artist, album, tracks=None):
    album_info = {'Artist name': artist.title(), 'Album Title': album.title()}
    if tracks is not None:
        album_info["No of tracks"] = tracks
    return album_info

while True:
    Artist = input("Enter artist name or quit : ")
    if Artist.lower() == "quit":
        break
    Album = input("Enter album title or quit : ")
    if Album.lower() == "quit":
        break
    track_input = input("Enter number of tracks (or press Enter to skip): ")

    if track_input:
        track = int(track_input)
    else:
        track = None
    
    print(make_album(artist=Artist,album=Album,tracks=track))