#build gui
import tkinter as tk
import pygame

pygame.init()

is_playing = False

def play_music():
    global is_playing
    if not is_playing:
        pygame.mixer.music.play()
        is_playing = True
def pause_music():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
def stop_music():
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False


window = tk.Tk()

play_button = tk.Button(window, text="播放", command=play_music)
play_button.pack()
pause_button = tk.Button(window, text="暫停", command=pause_music)
pause_button.pack()
stop_button = tk.Button(window, text="停止", command=stop_music)
stop_button.pack()

midi_filename = "generated_music.mid"
pygame.mixer.music.load(midi_filename)

window.mainloop()

pygame.quit()