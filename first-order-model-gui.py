from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import imageio, threading
from skimage.transform import resize
from time import sleep
from demo import load_checkpoints

size = (256, 256)
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                            checkpoint_path='./checkpoints/vox-cpk.pth.tar')

def stream(label, fps):
    while True:
        for image in resizedVideo:
            sleep(1 / fps)
            frame_image = ImageTk.PhotoImage(image)
            label.config(image=frame_image)
            label.image = frame_image

def resizeVideo(video):
    frames = []
    for frame in video:
        image = Image.fromarray(frame.astype('uint8'), 'RGB')
        image = image.resize(size)
        frames.append(image)
    return frames



def openSourceImage():
    global sourceImage
    root.filename = filedialog.askopenfilename(title="Select the source image",
                                               filetypes=(("Image files", "*.jpg"), ("All files", "*.*")))
    image = Image.open(root.filename)
    resizedImage = image.resize(size)
    sourceImage = ImageTk.PhotoImage(resizedImage)
    sourceImageLabel = Label(sourceImageFrame, image=sourceImage)
    sourceImageLabel.grid(row=1, column=0)

def openSourceVideo():
    global resizedVideo
    root.filename = filedialog.askopenfilename(title="Select the source video",
                                               filetypes=(("Video files", "*.mp4"), ("All files", "*.*")))
    video = imageio.get_reader(root.filename)
    fps = video.get_meta_data()['fps']
    resizedVideo = resizeVideo(video)
    sourceVideoLabel = Label(sourceVideoFrame)
    sourceVideoLabel.grid(row=1, column=0)
    thread = threading.Thread(target=stream, args=(sourceVideoLabel, fps,))
    thread.daemon = 1
    thread.start()


root = Tk()
root.title("First Order Model")

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
