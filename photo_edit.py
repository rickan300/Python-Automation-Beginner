import os
from PIL import Image, ImageFilter

source = '/Users/ricknarcisse/Desktop/photos/'
dest = '/Users/ricknarcisse/Desktop/edited_photos/'

for filename in os.listdir(source):
    img = Image.open(f"{source}/{filename}")
    fix = img.filter(ImageFilter.SHARPEN).convert('L')
    new_name = os.path.splitext(filename)

    fix.save(f"{dest}/{new_name}_fixed.jpeg")
