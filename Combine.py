import numpy as np
import cv2
import os

base = 'Worked/'
images = os.listdir(base)

for j in range(0,len(images), 50):
	output = cv2.imread(base+images[j])
	image1 = cv2.imread(base+images[j + 1])
	cv2.addWeighted(image1, 1.0/100, output, 1.0/100, 0, output)

	for i in range(j + 2,min(j + 100, len(images))):

		# load the image
		image1 = cv2.imread(base+images[i])
		cv2.addWeighted(image1, 1.0/min(100, len(images) - j), output, 1, 0, output)
	cv2.imwrite("Base/OutputComb" + str(j) + ".jpg", output)


