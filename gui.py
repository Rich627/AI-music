import tkinter as tk
import pygame
import os

#初始化pygame
pygame.mixer.init()

is_playing = False
current_music = ""
music_duration = 0

#利用pygame寫gui功能的函式
def play_music():
    global is_playing
    if not is_playing:
        pygame.mixer.music.unpause()
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

#建立視窗
window = tk.Tk()

#設定視窗標題
music_label = tk.Label(window, text="音樂名稱", font=("Helvetica", 12))
music_label.pack(pady=10)

#設定視窗大小以及按鈕
time_var = tk.StringVar()
time_label = tk.Label(window, textvariable=time_var, font=("Helvetica", 10))
time_label.pack()
play_button = tk.Button(window, text="播放", command=play_music)
play_button.pack(pady=10)
pause_button = tk.Button(window, text="暫停", command=pause_music)
pause_button.pack(pady=5)
stop_button = tk.Button(window, text="停止", command=stop_music)
stop_button.pack(pady=5)

#更新音樂資訊
def update_music_info():
    global current_music, music_duration
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() // 1000
        minutes = current_time // 60
        seconds = current_time % 60
        formatted_time = f"{minutes:02d}:{seconds:02d}"
        time_var.set(f"{formatted_time} / {music_duration}")
    window.after(1000, update_music_info)

#載入音樂
def load_music(filename):
    global current_music, music_duration
    pygame.mixer.music.load(filename)
    current_music = os.path.basename(filename)
    music_duration = pygame.mixer.Sound(filename).get_length() // 1
    music_label.config(text=current_music)
    time_var.set("00:00 / 00:00")

#開啟檔案對話框
def open_file_dialog():
    filename = tk.filedialog.askopenfilename(filetypes=[("MIDI Files", "*.mid")])
    if filename:
        load_music(filename)

#建立開啟檔案按鈕
open_button = tk.Button(window, text="開啟檔案", command=open_file_dialog)
open_button.pack(pady=5)


update_music_info()
window.mainloop()

