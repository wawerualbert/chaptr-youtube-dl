import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import threading

master = tk.Tk()
dest = StringVar()

def running(s):
	subprocess.call( s , shell=True , cwd = dest.get())

def download_video():
	if dest.get() is '':  # Check whether User chosen Destination or not
		destination_label.configure(text='Please Select Destination!')
	else:   
		link = e1.get()
		if link is '':  # Checking whether User gave Link or not
			destination_label.configure(text='Paste Link!')
			return
		else:     # Single Video Link Found and it will download
			cmd = 'youtube-dl -i ' + link.split('&')[0]
			th = threading.Thread(target=running, args=(cmd,))
			th.start()
			#subprocess.call(cmd, shell=True, cwd=dest.get())

def destination():  # Opening File Dialog to select Destination Folder
	global dest
	act = filedialog.askdirectory()
	dest.set(act)
	print(f'Selected directory : {dest.get()}')
	destination_label.configure(text=dest.get())

master.title("Chaptr Youtube Downloader")

tk.Label(master,text="Enter URL Here").grid(row=0)

e1 = tk.Entry(master , textvariable='Ctrl + V')
e1.grid(row=0, column=1)

tk.Button(master, text='Download Video', command=download_video).grid(row=3, column=1,sticky=tk.W,pady=4)
tk.Button(master, text='Select Destination', command=destination).grid(row=0, column=2,sticky=tk.W,pady=4)
destination_label = ttk.Label(master, text= "Chaptr Youtube-dl" , foreground = 'green' , background = 'white' ,font = ('Times New Roman' , 16 , 'bold'))
destination_label.grid(column = 6, row = 0 , sticky=tk.W,pady=4)

master.geometry("500x200")
ran = tk.Entry(master , width=10)

label = Label(master)
label.grid(row= 7 , column = 0)
tk.mainloop()
