import cv2

orb = cv2.ORB_create()

image = cv2.imread(image_path, 0)
kps, descs = orb.detectAndCompute(image, None)  # mask = None
outImg = cv2.drawKeypoints(image, kps, None, color=(0,255,0), flags = 0)