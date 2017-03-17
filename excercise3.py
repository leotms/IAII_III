'''
    File:        excercise3.py
    Description: Defines activities for Excercise 3.
    Authors:     Joel Rivas        #11-10866
                 Nicolas Manan     #06-39883
                 Leonardo Martinez #11-10576
    Updated:     03/17/2017
'''

from kmeans import *
from PIL import Image
import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("ERROR. Missing Arguments.")
        sys.exit()

    #get the name of the image to compress
    imgname = sys.argv[1]

    img = Image.open(imgname)

    #conver the image to get the rgb code for every pixel color
    rgb_img = img.convert('RGB')

    list_of_pixels = list(rgb_img.getdata())

    #parsing the data of the pixels to an array
    for i in range(len(list_of_pixels)):
        list_of_pixels[i] = list(list_of_pixels[i])

    #ranges for the compression
    ranges = [2, 4, 8, 16, 32, 64, 128]
    for i in ranges:

        print("Starting compression for %d clusters..."%(i))
        #get the data of the Kmeans algorithm
        c, J, k = k_means(list_of_pixels, i)

        print("Compression for %d clusters completed, saving new image..."%(i))

        for j in range(len(k)):
            new_arr = []
            for elem in k[j]:
                new_arr.append(int(round(elem)))
                k[j] = tuple(new_arr)

        new_list_of_pixels = []
        for pixel in c:
            new_list_of_pixels.append(k[pixel])

        new_image = Image.new(img.mode, img.size)
        new_image.putdata(new_list_of_pixels)

        name = imgname.split('.', 1)[0] + "[" + str(i) + "]"
        new_image.save(name,"PNG")

        print("Compression for %d clusters completed, saving new image..."%(i))

        new_image.show()
