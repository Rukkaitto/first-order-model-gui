from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import imageio, threading
from time import sleep


def stream(label):
    while True:
        for image in video.iter_data():
            sleep(0.02)
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

1

def openSourceImage():
    global sourceImage
    root.filename = filedialog.askopenfilename(title="Select a file",
                                               filetypes=(("Image files", "*.jpg"), ("All files", "*.*")))
    sourceImage = ImageTk.PhotoImage(Image.open(root.filename))
    sourceImageLabel = Label(sourceImageFrame, image=sourceImage).grid(row=1, column=0)


def openSourceVideo():
    global video
    root.filename = filedialog.askopenfilename(title="Select a file",
                                               filetypes=(("Video files", "*.mp4"), ("All files", "*.*")))
    video = imageio.get_reader(root.filename)
    sourceVideoLabel = Label(sourceVideoFrame)
    sourceVideoLabel.grid(row=1, column=0)
    thread = threading.Thread(target=stream, args=(sourceVideoLabel,))
    thread.daemon = 1
    thread.start()


root = Tk()

sourcesFrame = LabelFrame(root, text="Source input")
sourcesFrame.pack(padx=10, pady=10)

# Source Image
sourceImageFrame = Frame(sourcesFrame, padx=50, pady=50)
sourceImageFrame.grid(row=0, column=0)

sourceImageLabel = Label(sourceImageFrame, text="Source image")
sourceImageLabel.grid(row=0, column=0)

sourceImageButton = Button(sourceImageFrame, text="Browse...", command=openSourceImage)
sourceImageButton.grid(row=2, column=0)

# Source Video

sourceVideoFrame = Frame(sourcesFrame, padx=50, pady=50)
sourceVideoFrame.grid(row=0, column=1)

sourceVideoLabel = Label(sourceVideoFrame, text="Source video")
sourceVideoLabel.grid(row=0, column=0)

sourceVideoButton = Button(sourceVideoFrame, text="Browse...", command=openSourceVideo)
sourceVideoButton.grid(row=2, column=0)

root.mainloop()
