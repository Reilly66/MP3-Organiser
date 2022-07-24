import sys
import os
import pickle

library = []
playlists = []

class Song:
    def __init__(self, title, artist, genre, length):
        if library == []:
            self.id = 0
        else:
            self.id = library[-1].id + 1
        self.title = title
        self.artist = artist
        self.genre = genre
        self.length = length
        self.favourite = False
    
    def toggle_favourite(self):
        self.favourite = not self.favourite

class Playlist:
    def __init__(self, name, description):
        if playlists == []:
            self.id = 0
        else:
            self.id = playlists[-1].id + 1
        self.name = name
        self.description = description
        self.songs = []

def main_menu():
    print("--MP3 Organiser--")
    print("1) Song Manager")
    print("2) Playlist Manager")
    print("3) Exit")
    choice = input(": ")
    if choice == 1:
        song_menu()
    elif choice == 2:
        playlist_menu()
    elif choice == 3:
        update()
        sys.exit()
    else:
        main_menu()

def song_menu():
    print("--Song Menu--")
    print("1) Add song to library")
    print("2) Modify song in library")
    print("3) Remove song from library")
    print("4) Toggle song as favourite")
    print("5) Exit to main menu")
    choice = input(": ")
    if choice == 1:
        create_song()
    elif choice == 2:
        modify_song
    elif choice == 3:
        delete_song()
    elif choice == 4:
        toggle_song_favourite()
    elif choice == 5:
        main_menu()
    else:
        song_menu()

def create_song():
    song_title = input("Enter song title: ")
    song_artist = input("Enter artist: ")
    song_genre = input("Enter the song genre: ")
    song_length = int(input("Enter song length (seconds): "))
    new_song = Song(song_title, song_artist, song_genre, song_length)
    library.append(new_song)
    update()
    song_menu()

def modify_song():
    for i in range(len(library)):
        song = library[i]
        print(f"{song.id}) {song.title} - {song.artist}")
    id = int(input("Enter song id: "))
    index = -1
    for i in range(len(library)):
        if id == library[i].id:
            index = i
    if index == -1:
        print("Song does not exist")
        song_menu()
    selected_song = library[index]
    print("1) Change title")
    print("2) Change artist")
    print("3) Change genre")
    print("4) Change length (seconds)")
    choice = int(input(": "))
    modification = input("Enter new value: ")
    if choice == 1:
        selected_song.title = modification
    elif choice == 2:
        selected_song.artist = modification
    elif choice == 3:
        selected_song.genre = modification
    elif choice == 4:
        selected_song.length = int(modification)
    else:
        song_menu()
    library[index] = selected_song
    update()
    song_menu()

def delete_song():
    for i in range(len(library)):
        song = library[i]
        print(f"{song.id}) {song.title} - {song.artist}")
    id = int(input("Enter song id: "))
    index = -1
    for i in range(len(library)):
        if id == library[i].id:
            index = i
    if index == -1:
        print("Song does not exist")
        song_menu()
    library.pop(index)
    update()
    song_menu()

def toggle_song_favourite():
    for i in range(len(library)):
        song = library[i]
        print(f"{song.id}) {song.title} - {song.artist}")
    id = int(input("Enter song id: "))
    index = -1
    for i in range(len(library)):
        if id == library[i].id:
            index = i
    if index == -1:
        print("Song does not exist")
        song_menu()
    selected_song = library[index]
    selected_song.toggle_favourite()
    library[index] = selected_song()
    update()
    song_menu()

def playlist_menu():
    print("1) Create new playlist")
    print("2) Delete playlist")
    print("3) Add song to playlist")
    print("4) Remove song from playlist")
    print("5) Main menu")
    choice = int(input(": "))
    if choice == 1:
        create_playlist()
    elif choice == 2:
        delete_playlist()
    elif choice == 3:
        add_song_playlist
    elif choice == 4:
        remove_song_playlist()
    elif choice == 5:
        main_menu()

def create_playlist():
    name = input("Enter playlist name: ")
    description = input("Enter playlist description: ")
    new_playlist = Playlist(name, description)
    playlists.append(new_playlist)
    update()
    playlist_menu()

def delete_playlist():
    for i in range(len(playlists)):
        playlist = playlists[i]
        print(f"{playlist.id}) {playlist.name} - {playlist.description}")
    id = int(input("Enter playlist id: "))
    index = -1
    for i in range(len(playlists)):
        if id == playlists[i].id:
            index = i
    if index == -1:
        print("Playlist does not exist")
        playlist_menu()
    playlists.pop(index)
    update()
    playlist_menu()

def add_song_playlist():
    for i in range(len(playlists)):
        playlist = playlists[i]
        print(f"{playlist.id}) {playlist.name}")
    id = int(input("Enter playlist id: "))
    playlist_index = -1
    for i in range(len(playlists)):
        if id == playlists[i].id:
            playlist_index = i
    if playlist_index == -1:
        print("Playlist does not exist")
        playlist_menu()
    selected_playlist = playlists[playlist_index]

    for i in range(len(library)):
        song = library[i]
        print(f"{song.id}) {song.title} - {song.artist}")
    id = int(input("Enter song id: "))
    index = -1
    for i in range(len(library)):
        if id == library[i].id:
            index = i
    if index == -1:
        print("Song does not exist")
        song_menu()
    selected_song = library[index]

    selected_playlist.songs.append(selected_song.id)
    playlists[playlist_index] = selected_playlist
    update()
    playlist_menu()

def remove_song_playlist():
    for i in range(len(playlists)):
        playlist = playlists[i]
        print(f"{playlist.id}) {playlist.name}")
    id = int(input("Enter playlist id: "))
    playlist_index = -1
    for i in range(len(playlists)):
        if id == playlists[i].id:
            playlist_index = i
    if playlist_index == -1:
        print("Playlist does not exist")
        playlist_menu()
    selected_playlist = playlists[playlist_index]

    for i in range(len(library)):
        song = library[i]
        print(f"{song.id}) {song.title} - {song.artist}")
    id = int(input("Enter song id: "))
    index = -1
    for i in range(len(library)):
        if id == library[i].id:
            index = i
    if index == -1:
        print("Song does not exist")
        song_menu()
    selected_playlist.songs.pop(index)
    playlists[playlist_index] = selected_playlist
    update()
    playlist_menu()

def update():
    with open("library", "wb") as f:
        pickle.dump(library, f)

    with open("playlists", "wb") as f:
        pickle.dump(playlists, f)
   
if __name__ == "__main__":
    if os.path.exists("library"):
        with open("library", "rb") as f:
            library = pickle.load(f)
    if os.path.exists("playlists"):
        with open("playlists", "rb") as f:
            playlists = pickle.load(f)
    main_menu()
