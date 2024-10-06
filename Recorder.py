from tkinter import *
import pyscreenrec
from PIL import Image

root = Tk()
root.title("screen recorder")
root.config(bg="#fff")
root.geometry("400x600")
root.resizable(False, False)
img_ico = PhotoImage(file="image/icon.png")
root.iconphoto(False, img_ico)
font1 = ("Tajwal", 12, "bold")
image = Image.open("image/pause.png")
small_image = image.resize((50, 50))
small_image.save("image/new_pause.png")

def start():
    file = fileName.get()
    rec.start_recording(str(file+".mp4"),5)
def pause():
    rec.pause_recording()
def resume():
    rec.resume_recording()
def stop():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()

L1 = Label(root, text="Screen Recorder", bg="white", font=font1)
L1.pack(pady=10)

fileName = StringVar()
entry = Entry(root, textvariable=fileName, width=18, font=font1)
entry.pack(pady=10)

img_rec = PhotoImage(file="image/rec.png")
Label(root, image=img_rec, bd=0, width=400, height=400).pack(pady=8)

Btn_pause = Button(root, bd=0, text="Pause", width=10, font=font1 , cursor="hand2", command=pause)
Btn_pause.place(x=30, y=500)

Btn_play = Button(root, bd=0, text="Resume", width=10, font=font1 , cursor="hand2", command=resume)
Btn_play.place(x=150, y=500)

Btn_resume = Button(root, bd=0, text="Stop", width=10, font=font1 , cursor="hand2", command=stop)
Btn_resume.place(x=270, y=500)

Btn_Start = Button(root, text="Start", bd=2, cursor="hand2", width=20, font=font1, command=start)
Btn_Start.place(x=100, y=550)

root.mainloop()