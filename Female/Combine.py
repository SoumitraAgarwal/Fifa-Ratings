import numpy as np
import cv2
import os

base = 'Pictures/'
images = os.listdir(base)
images = images[:100]
output = cv2.imread(base+images[0])
image1 = cv2.imread(base+images[1])
cv2.addWeighted(image1, 0.012, output, 0.012, 0, output)

for i in range(2,len(images)):

	# load the image
	image1 = cv2.imread(base+images[i])
	cv2.addWeighted(image1, 0.012, output, 1, 0, output)
print(output)
cv2.imwrite("Output1.jpg", output)
