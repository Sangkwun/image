import numpy as np
from sklearn.cluster import KMeans
import cv2

img = cv2.imread("../../Caffe_data/가비터/3.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.reshape((img.shape[0] * img.shape[1], 3))
clt = KMeans(n_clusters=5)
clt.fit(img)


def centroid_histogram(clt):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins=numLabels)

	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()

	# return the histogram
	return hist

hist = centroid_histogram(clt)
print(hist)
print(clt.cluster_centers_)
