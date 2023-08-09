import threading
from pytube import Playlist

def download_video(video, download_path='.'):
    print(f"Downloading {video.title}...")
    video.streams.get_highest_resolution().download(output_path=download_path)
    print(f"Downloaded {video.title} successfully!")

def download_videos_from_playlist(playlist_url, download_path='.'):
    # Create a Playlist object
    playlist = Playlist(playlist_url)

    # List to hold all threads
    threads = []

    # Iterate over all videos in the playlist and start downloading them in separate threads
    for video in playlist.videos:
        thread = threading.Thread(target=download_video, args=(video, download_path))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All videos downloaded successfully!")

if __name__ == "__main__":
    
    playlist_link = 'ENTER_THE_ENTIRE_LINK_TO_THE_YOUTUBE_PLAYLIST'
    
    # Specify the download path if you want, default is current directory
    path = '.'

    download_videos_from_playlist(playlist_link, path)
