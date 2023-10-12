import subprocess
import os  # Import the os module to handle file paths

def download_video(url):
    try:
        # Set the options for youtube-dl
        options = [
            'youtube-dl',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '0',  # Choose the best audio quality
            '--output', '/Users/nuns/desktop/music/%(title)s.%(ext)s',  # Save in the 'music' folder
            url
        ]

        # Run youtube-dl to download the video as MP3
        subprocess.run(options, check=True)

        print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download_playlist(playlist_url):
    try:
        # Set the options for youtube-dl to download the entire playlist as MP3
        options = [
            'youtube-dl',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '0',  # Choose the best audio quality
            '--yes-playlist',  # Download entire playlist
            '--output', '/Users/nuns/desktop/music/%(title)s.%(ext)s',  # Save in the 'music' folder
            playlist_url
        ]

        # Run youtube-dl to download the playlist as MP3
        subprocess.run(options, check=True)

        print("Playlist download complete.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    choice = input("Enter 'v' to download a single video or 'p' to download a playlist: ")
    
    if choice == 'v':
        youtube_url = input("Enter the YouTube video URL: ")
        download_video(youtube_url)
    elif choice == 'p':
        playlist_url = input("Enter the YouTube playlist URL: ")
        download_playlist(playlist_url)
    else:
        print("Invalid choice. Please enter 'v' or 'p'.")
