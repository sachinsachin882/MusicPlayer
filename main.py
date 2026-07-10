import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init()

playlist = []
current_song = 0

def load_songs():
    global playlist
    files = filedialog.askopenfilenames(
        filetypes=[("Audio Files", "*.mp3 *.wav")]
    )
    for file in files:
        playlist.append(file)
        listbox.insert(tk.END, os.path.basename(file))

def play_song():
    global current_song
    if playlist:
        current_song = listbox.curselection()[0]
        pygame.mixer.music.load(playlist[current_song])
        pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    if playlist:
        current_song = (current_song + 1) % len(playlist)
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(current_song)
        play_song()

def previous_song():
    global current_song
    if playlist:
        current_song = (current_song - 1) % len(playlist)
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(current_song)
        play_song()

def add_song():
    file = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav")]
    )
    if file:
        playlist.append(file)
        listbox.insert(tk.END, os.path.basename(file))

def delete_song():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        playlist.pop(index)

root = tk.Tk()
root.title("Music Player")
root.geometry("400x450")

listbox = tk.Listbox(root, width=50, height=12)
listbox.pack(pady=10)

tk.Button(root, text="Load Songs", command=load_songs).pack(fill="x")
tk.Button(root, text="Play", command=play_song).pack(fill="x")
tk.Button(root, text="Pause", command=pause_song).pack(fill="x")
tk.Button(root, text="Resume", command=resume_song).pack(fill="x")
tk.Button(root, text="Stop", command=stop_song).pack(fill="x")
tk.Button(root, text="Previous", command=previous_song).pack(fill="x")
tk.Button(root, text="Next", command=next_song).pack(fill="x")
tk.Button(root, text="Add Song", command=add_song).pack(fill="x")
tk.Button(root, text="Delete Song", command=delete_song).pack(fill="x")

root.mainloop()