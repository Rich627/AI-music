import tkinter as tk
import pygame


# 初始化 pygame
pygame.mixer.init()

is_playing = False
music_duration = 0


# 通過 Pygame 實現 GUI
def play_music():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('/Users/rich/Desktop/AI-music/generated_music.mid')
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


# 創建窗口
window = tk.Tk()

# 設置窗口大小和按鈕
play_button = tk.Button(window, text="播放", command=play_music)
play_button.pack(pady=10)
pause_button = tk.Button(window, text="暫停", command=pause_music)
pause_button.pack(pady=5)
stop_button = tk.Button(window, text="停止", command=stop_music)
stop_button.pack(pady=5)

window.mainloop()





