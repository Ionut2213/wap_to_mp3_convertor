# What imports we need and what libraries are we gonna use
import os
from tkinter import Tk, Label, Button, filedialog, StringVar, Entry
# if you don t have tkinter installed use the command pip install tkinter

# Another library that we gonne use for audio files is pydub
# Command to install it pip install pydub
from pydub import AudioSegment


# block of cod for making the app functional

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV Files","*.wav")])
    if file_path:
        input_file.set(file_path)







# Setting the main window of the app

root = Tk()
root.title("App to convert WAV to MP3")
root.geometry("600x300")

input_file = StringVar()


Label(root, text="Select the WAV file:").pack(pady=5)
Entry(root, textvariable=input_file, width=40).pack(pady=5)
Button(root, text="Select the file", command=select_input_file).pack(pady=5)


Label(root, text="Select destination folder: ").pack(pady=5)
Entry(root, textvariable=None, width=40).pack(pady=5)
Button(root, text="Select folder destination", command=None).pack(pady=5)

Button(root, text="Convert", command=None).pack(pady=10)
Label(root, textvariable=None, fg="blue").pack(pady=5)





root.mainloop()