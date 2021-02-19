import cv2
import numpy as np

orb = cv2.ORB_create()

image = cv2.imread(image_path, 0)

# mask
mask_file = open('mask_file.txt', 'r')
mask_list = mask_file.readlines()
mask_line_list = mask_list[image_index].split()
mask = np.ones_like(image) * 255
for i in range(int(len(mask_line_list)/4)):
    x1 = int(mask_line_list[4*i])
    y1 = int(mask_line_list[4*i+1])
    x2 = int(mask_line_list[4*i+2])
    y2 = int(mask_line_list[4*i+3])
    mask[y1:y2, x1:x2] = 0

#  detect and draw   
kps, descs = orb.detectAndCompute(image, mask)  
outImg = cv2.drawKeypoints(image, kps, None, color=(0,255,0), flags = 0)  
cv2.imshow('Out image', outImg)    
cv2.waitKey(0)
cv2.destroyAllWindows()
 