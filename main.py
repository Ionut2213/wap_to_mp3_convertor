# What imports we need and what libraries are we gonna use
import os
from tkinter import Tk, Label, Button, filedialog, StringVar, Entry
# if you don t have tkinter installed use the command pip install tkinter

# Another library that we gonne use for audio files is pydub
# Command to install it pip install pydub
from pydub import AudioSegment










# Setting the main window of the app

root = Tk()
root.title("App to convert WAV to MP3")
root.geometry("600x300")




root.mainloop()