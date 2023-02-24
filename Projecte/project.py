import os
import cv2
import time
path = "images/"
images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter("friendship.avi", fourcc, 30 , (width, height))
for i in range(0,count-1):
    img = cv2.imread(images[i])
    out.write(img)
out.release()
# sorry about how fast the video goes, i dont know how to extend it besides just making a bunch of copies
#of the one image.