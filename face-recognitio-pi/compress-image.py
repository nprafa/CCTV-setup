#this script reduces the 

from PIL import Image
import PIL
import os
import glob

#sample working code
#file_name = 'sample.jpeg'
#picture = Image.open('sample.jpeg')
#dim = picture.size
#print(f"This is the current width and height of the image: {dim}")
#picture.save("Compressed_"+file_name,optimize=True,quality=30) 

image_dir = "tocompress/"
filepath = "faces/data/"

for name in os.listdir(image_dir):
    for filename in os.listdir(f"{image_dir}/{name}"):
        pic_path = image_dir + name + "/" + filename
        picture = Image.open(pic_path)
        newfilename = "compressed_" + filename
        picture.save(filepath+name+"/"+newfilename,optimize=True,quality=30)

#reopen and save the compressed file

for name in os.listdir(filepath):
    for filename in os.listdir(f"{filepath}/{name}"):
        pic_path = filepath+name+"/"+filename
        picture = Image.open(pic_path)
        picture = picture.rotate(270)
        picture.save(pic_path)
