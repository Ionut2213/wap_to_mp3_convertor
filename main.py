# What imports we need and what libraries are we gonna use
import os
from tkinter import Tk, Label, Button, filedialog, StringVar, Entry
# if you don t have tkinter installed use the command pip install tkinter

# Another library that we gonne use for audio files is pydub
# Command to install it pip install pydub
from pydub import AudioSegment


# block of cod for making the app functional

def convert_wav_to_mp3(input_wav, output_mp3):
    try:
        sound = AudioSegment.from_wav(input_wav)
        sound.export(output_mp3, format="mp3")
        return True
    except Exception as e:
        print(f"Conversion Error:{e}")
        return False

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV Files","*.wav")])
    if file_path:
        input_file.set(file_path)


def select_output_file():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder.set(folder_path)


def start_conversion():
    input_path = input_file.get()
    output_path = os.path.join(output_folder.get(), os.path.splitext(os.path.basename(input_path))[0] + ".mp3")

    if not input_path or not output_folder.get():
        status.set("Please select a file and a destination file")
        return
    status.set("Conversion started...")
    success = convert_wav_to_mp3(input_path, output_path)

    if success:
        status.set(f"Conversion completed: {output_path}")
    else:
        status.set("Conversion Error")







# Setting the main window of the app

root = Tk()
root.title("App to convert WAV to MP3")
root.geometry("600x300")

input_file = StringVar()
output_folder = StringVar()
status = StringVar()


Label(root, text="Select the WAV file:").pack(pady=5)
Entry(root, textvariable=input_file, width=40).pack(pady=5)
Button(root, text="Select the file", command=select_input_file).pack(pady=5)


Label(root, text="Select destination folder: ").pack(pady=5)
Entry(root, textvariable=output_folder, width=40).pack(pady=5)
Button(root, text="Select folder destination", command=select_output_file).pack(pady=5)

Button(root, text="Convert", command=start_conversion).pack(pady=10)
Label(root, textvariable=status, fg="blue").pack(pady=5)





root.mainloop()