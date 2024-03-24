import tkinter as tk
import customtkinter
from pytube import YouTube
import threading

def startDownload():
    thread = threading.Thread(target=download_video)
    thread.start()

def download_video():
    try:
        yt = url_var.get()
        yd = YouTube(yt, on_progress_callback=on_progress)
        video = yd.streams.get_highest_resolution()

        title.configure(text=yt.title, text_color="white")
        finishlabel.configure(text="")
        video.download(r'C:\Users\hp\Videos\Youtube Videos')

        finishlabel.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        finishlabel.configure(text="Download Error!", text_color="red")
        print("Error:", e)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    percentage.configure(text=per + '%')
    percentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

# System setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Adding UI
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url_var)
link.pack()

# Finish Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress Percentage
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run App
app.mainloop()
