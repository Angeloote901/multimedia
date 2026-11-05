import sqlite3
import pyglet
import os

def create_table():
    # Create a table for music metadata
    conn = sqlite3.connect('music.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='music'
    ''')
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE music (
                id INTEGER PRIMARY KEY,
                title TEXT,
                artist TEXT,
                album TEXT,
                file_path TEXT
            )
        ''')
    conn.commit()
    conn.close()

def insert_song(title, artist, album, file_path):
    # Insert a song into the database
    print(f"Inserting song: {title} by {artist} from album {album}")
    conn = sqlite3.connect('music.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO music (title, artist, album, file_path)
        VALUES (?, ?, ?, ?)
    ''', (title, artist, album, file_path))
    conn.commit()
    conn.close()

def play_song(file_path):
    print(f"Playing song: {file_path}")
    # Play an audio file using pyglet
    media = pyglet.media.load(file_path, streaming=False)
    media.play()
    pyglet.app.run()

def load_songs():
    # Load the MP3 songs from the songs directory
    print("Loading songs from the 'songs' directory...")
    for file in os.listdir('songs'):
        if file.endswith('.mp3'):
            title = file.split('.')[0]
            artist = 'TheFatRat'
            album = 'No Album'
            file_path = 'songs/' + file
            insert_song(title, artist, album, file_path)

def main():
    create_table()
    load_songs()
    play_song('songs/fly_away.mp3')

if __name__ == "__main__":
    main()