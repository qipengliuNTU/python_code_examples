import glob
import cv2

images_path = sorted(glob.glob('../0_datasets/new_college/Images/*.jpg'))

images = []
for image_path in images_path:
    image = cv2.imread(image_path)
    images.append(image)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()