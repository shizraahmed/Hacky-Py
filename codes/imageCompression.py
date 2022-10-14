import PIL
from PIL import Image
from tkinter.filedialog import *

fl = askopenfilenames()
img = Image.open(fl[0])
img.save("compressed1.jpg", "JPEG", optimize=True, quality=10)
Image.open("compressed.jpg")
