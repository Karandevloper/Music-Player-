import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.current_dir = os.getcwd()
        self.playlist = []
        self.current_track = 0
        self.paused = False

        self.create_ui()

        # Initialize pygame mixer
        pygame.mixer.init()

    def create_ui(self):
        # Create playlist box
        self.playlist_box = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.playlist_box.pack(pady=20)

        # Create buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)

        self.btn_add = tk.Button(control_frame, text="Add Music", command=self.add_track)
        self.btn_add.grid(row=0, column=0, padx=10)

        self.btn_remove = tk.Button(control_frame, text="Remove Music", command=self.remove_track)
        self.btn_remove.grid(row=0, column=1, padx=10)

        self.btn_prev = tk.Button(control_frame, text="Previous", command=self.prev_track)
        self.btn_prev.grid(row=1, column=0, pady=10)

        self.btn_playpause = tk.Button(control_frame, text="Play", command=self.play_pause)
        self.btn_playpause.grid(row=1, column=1, pady=10)

        self.btn_next = tk.Button(control_frame, text="Next", command=self.next_track)
        self.btn_next.grid(row=1, column=2, pady=10)

    def add_track(self):
        track = filedialog.askopenfilename(initialdir=self.current_dir, title="Choose a track", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if track:
            self.playlist.append(track)
            self.playlist_box.insert(tk.END, os.path.basename(track))

    def remove_track(self):
        selected_index = self.playlist_box.curselection()
        if selected_index:
            self.playlist.pop(selected_index[0])
            self.playlist_box.delete(selected_index)

    def play_pause(self):
        if self.playlist:
            if pygame.mixer.music.get_busy() and not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
                self.btn_playpause.config(text="Resume")
            else:
                if self.paused:
                    pygame.mixer.music.unpause()
                    self.paused = False
                else:
                    self.play_track()

    def play_track(self):
        if self.playlist:
            track = self.playlist[self.current_track]
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            self.btn_playpause.config(text="Pause")

    def prev_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play_track()

    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_track()

def main():
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

