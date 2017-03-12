
from kmeans import *
from PIL import Image

imgname = 'data/E3/AfghanGirlEye.jpg'
img = Image.open(imgname)
#img = Image.open('data/E3/Tipasexy_1_rubia_Obvio.jpg')

rgb_img = img.convert('RGB')

print(img.size)
print(rgb_img.size)

list_of_pixels = list(rgb_img.getdata())
print(len(list_of_pixels))
print(list_of_pixels[0])
print(type(list_of_pixels[0]))

for i in range(len(list_of_pixels)):
    list_of_pixels[i] = list(list_of_pixels[i])

print(list_of_pixels[0])
print(type(list_of_pixels[0]))


ranges = [2, 4, 8, 16, 32, 64, 128]
for i in ranges:

    c, J, k = k_means(list_of_pixels, i)

    print("Asignacion para %d clusters"%(i))
    print(c)
    print(k)

    for i in range(len(k)):
        new_arr = []
        for elem in k[i]:
            new_arr.append(int(round(elem)))
            k[i] = tuple(new_arr)

    new_list_of_pixels = []
    for pixel in c:
        new_list_of_pixels.append(k[pixel])

    new_image = Image.new(img.mode, img.size)
    new_image.putdata(new_list_of_pixels)

    print("Image: ", i)
    

    name = imgname[:-4] + "[" + str(i) + "]" + ".jpg"
    new_image.save(name)

    new_image.show()