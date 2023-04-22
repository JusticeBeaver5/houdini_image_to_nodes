from PIL import Image
import hou
import time

start = time.perf_counter()
dir = 'D:\\python\\image_processing\\'

obj = hou.node('/obj')

with Image.open(f'{dir}thats_what_she_said3.jpg') as img:
    px = img.load()

width, height = img.size

print(width, height)
# print(img.getpixel((1, 10)))
# px_color = img.getpixel((68, 59))



for i in range(width):
    for j in range(height):
        # print(i, j)
        px_color = img.getpixel((i, j))
        print(px_color)
        null = obj.createNode('null',f'null_{i}_{j}')
        null.setPosition([i*0.75, -j/2])
        null.setColor(hou.Color(px_color[0]/255, px_color[1]/255, px_color[2]/255))


print(f'execution time = {time.perf_counter() - start} ')