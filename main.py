import os, sys
from PIL import Image

im = Image.open("fox.jpg")
print ("/* Image Width:%d Height:%d */", im.size[0], im.size[1])
path = os.getcwd()
files = os.listdir(path)
file = open('output.txt', 'w')
file.write("unsigned short image[] = {\n")
print ("unsigned short image[] = {")
pix = im.load()  # load pixel array
for h in range(im.size[1]):
    for w in range(im.size[0]):
        if w < im.size[0]:
            print(w)
            print(h)
            R = pix[w, h][0] >> 3
            G = pix[w, h][1] >> 2
            B = pix[w, h][2] >> 3
            rgb = (R << 11) | (G << 5) | B
            print(hex(rgb))
            file.write(hex(rgb)+ ",\n")
        else:
            rgb = 0
            print("0x0,")
print("};")
file.write("};")
file.close()
