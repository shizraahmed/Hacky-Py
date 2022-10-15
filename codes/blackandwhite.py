from PIL import Image
import os

ext = ("jpg", "png", "ico", "gif", "svg")

path = "~/"

li = os.listdir(path)

for i in li:
    if i.endswith(ext):
        color_image = Image.open(path + i)
        bw = color_image.convert('L')
        bw.save(path + i)
