from tkinter import *   # For the application window
from tkinter import ttk # For the application window
from tkinter import messagebox
import yt_dlp
import vlc
import os
import pygame
import threading
from youtube_search import YoutubeSearch

class App:
    def __init__(self):
        self.player = None
        self.audio_file = None
        self.bootup()
        
    def bootup(self):
        self.draw_display()

    # Window
    def draw_display(self):
        self.display = Tk()
        self.display.title("YouTube Audio Player")
        self.display.geometry("500x200")
        self.display.configure(background='#00FF00')

        # Label
        self.label = Label(self.display, text="Enter YouTube URL or Song Name:", bg='#00FF00')
        self.label.pack(pady=10)

        # Entry field
        self.entry = Entry(self.display, width=60)
        self.entry.pack(pady=5)

        # Play Button
        self.play_button = Button(self.display, text="Play", command=self.start_audio_thread)
        self.play_button.pack(pady=10)

        # Stop Button
        self.stop_button = Button(self.display, text="Stop", command=self.stop_audio)
        self.stop_button.pack(pady=5)

        self.display.mainloop()

    def start_audio_thread(self):
        thread = threading.Thread(target=self.download_and_play_audio)
        thread.start()

    def download_and_play_audio(self):
        query = self.entry.get()
        if not query:
            messagebox.showerror("Input Error", "Please enter a URL or search term.")
            return
        
        try:
            url = self.get_youtube_url(query)
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'no_warnings': True,
                'outtmpl': 'temp.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                self.audio_file = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            
            self.play_audio(self.audio_file)
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_youtube_url(self, query):
        if "youtube.com" in query or "youtu.be" in query:
            return query
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            raise Exception("No results found.")
        video_id = results[0]['id']
        return f"https://www.youtube.com/watch?v={video_id}"

    def play_audio(self, file_path):
        if self.player:
            self.player.stop()
        self.player = vlc.MediaPlayer(file_path)
        self.player.play()

    def stop_audio(self):
        if self.player:
            self.player.stop()
        if self.audio_file and os.path.exists(self.audio_file):
            os.remove(self.audio_file)
            self.audio_file = None
        
if __name__ == '__main__':
    App()