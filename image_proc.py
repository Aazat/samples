import cv2
import sys
import numpy as np

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"  # len is 65

img = cv2.imread(cv2.samples.findFile("Data/apple.jpg"))
if img is None:
    sys.exit("Could not readthe image.")

# cv2.imshow("Display window", img)
# k = cv2.waitKey(0)

def brighten(img_array):
    insert = []
    for row in img_array:
        insert_row = []
        for pixel in row:
            brightness = np.mean(pixel)
            insert_row.append(brightness)
            #print(pixel, brightness, insert_row)
        insert.append(insert_row)
        
    return insert

pixel_mat = brighten(img)
#print(pixel_mat[100][100])

