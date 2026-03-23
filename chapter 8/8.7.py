'''Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number of 
tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.'''


def make_album(artist, album, tracks=None):
    album_info = {'Artist name': artist.title(), 'Album Title': album.title()}
    if tracks:
        album_info["No of tracks"] = tracks
    return album_info

print(make_album(artist="parmish verma",album="superstar"))
print(make_album(artist="parmish verma",album="off limits"))
print(make_album(artist="parmish verma",album="superstar",tracks=5))