from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    link = entry.get()
    path = filedialog.askdirectory()
    if not link or not path:
        messagebox.showerror("Error", "Please enter URL and choose a folder!")
        return
    try:
        yt = YouTube(link)
        # Progressive = includes both video & audio (max ~720p)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        messagebox.showinfo("Downloading", f"Downloading: {yt.title} ({stream.resolution})")
        stream.download(path)
        messagebox.showinfo("Success", f"Downloaded:\n{yt.title}\nSaved in:\n{path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

root = tk.Tk()
root.title("YouTube Video Downloader (720p)")
root.geometry("420x220")

tk.Label(root, text="Enter YouTube Video URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=55)
entry.pack(pady=5)
tk.Button(root, text="Download Video", bg="red", fg="white", command=download_video).pack(pady=10)

root.mainloop()
