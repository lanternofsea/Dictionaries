# Dictionary of Song Artists (Key) and a list of their songs(values)
fav_artists = {"Ed Sheeran":["Shape of you", "Perfect"], "Bruno Mars": ["The Lazy Song", "Uptown Funk"]}

for i in range(5):
    # Ask user to enter artist name
    artist = input("Enter Artist Name: ")
    # ask user to enter songs by that artist as a string
    songs = input("Enter songs by artist (comma separated): ")

    # List of songs my the artist
    song_list = songs.split(",")

    # Your single line code to add the artist(key) and song_list(value) to the dictionary fav_artists
    fav_artists[artist] = [songs]

# Your single code to delete the key value pair for Bruno Mars in next line
del fav_artists['Bruno Mars']

# Your code to iterate over the keys and values in dictionary fav_artists using .items() in next line
for artist, songs in fav_artists.items():
    print(f"Artist: {artist} Songs: {songs}")

# Your single line code to print out the list of keys in the fav_artists dictionary using .keys() in next line
print(fav_artists.keys())

# Your single line code to print out the list of all the values in the resulting dictionary using .values() in next line
print(fav_artists.values())