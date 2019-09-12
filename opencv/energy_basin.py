import cv2 as cv
import numpy as np


def getEnergyMap(dimg, thresholds):
	cv.normalize(dimg, dimg, 0, 1.0, cv.NORM_MINMAX)
	timg = np.zeros(dimg.shape, dtype=np.float)
	tmp = np.zeros(dimg.shape, dtype=np.float)

	for t_hold in thresholds:
		_, tmp = cv.threshold(dimg, t_hold, 1.0, cv.THRESH_BINARY)
		timg +=tmp
		
	cv.normalize(timg, timg, 0, 1.0, cv.NORM_MINMAX)
	return timg



def main():
	h = 800
	w =1600
	img = np.zeros((h, w), dtype=np.uint8)

	u_left = (w//2-w//4, h//2-h//4)
	d_right = (w//2+w//4, h//2+h//4)
	cv.rectangle(img, u_left, d_right, 255, -1)

	img = cv.distanceTransform(img, cv.DIST_L2, 5)
	cv.normalize(img, img, 0, 1.0, cv.NORM_MINMAX)
	
	img = getEnergyMap(img, np.linspace(0, 1, 11))
	cv.imshow("Energy Map", img)
	cv.waitKey(0)

if __name__ == '__main__':
	main()