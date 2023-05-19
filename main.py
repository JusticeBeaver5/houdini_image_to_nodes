from PIL import Image
import hou
import time
from threading import Thread

dir = 'D:\\python\\image_processing\\'

obj = hou.node('/obj')

with Image.open(f'{dir}thats_what_she_said4.jpg') as img:
    px = img.load()

width, height = img.size

print(width, height)


def createMosaic(img, width, height):
    start = time.perf_counter()
    for i in range(height):
        for j in range(width):
            px_color = img.getpixel((j, i))
            null = obj.createNode('null',f'_{i}_{j}')
            null.setPosition([j*0.75, -i/2])
            null.setColor(hou.Color(px_color[0]/255, px_color[1]/255, px_color[2]/255))
    print(f'execution time = {time.perf_counter() - start} ')

    
th = Thread(target=createMosaic, args=[img, width, height], daemon=True)
th.start()