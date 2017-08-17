
from PIL import Image
from PIL import ImageChops
import numpy as np

print(123)
im1 = Image.open("P1.png")
arr1 = np.array(im1)

im2 = Image.open("P2.png")
arr2 = np.array(im2)

length = arr1.shape
ans = np.zeros(length,dtype = int )

for i in range(length[0]):
	for j in range(length[1]):
		if not np.array_equal(arr1[i][j],arr2[i][j]):
			ans[i][j] = arr2[i][j]

"""
im1 = Image.open("P1.png")
im2 = Image.open("P2.png")

diff = ImageChops.difference(im1, im2)
diffarray = np.array(diff)
arr2 = np.array(im2)

length = diffarray.shape
for i in range(length[0]):
	for j in range(length[1]):
		if not np.array_equal(diffarray[i][j],[0,0,0,0]):
			diffarray[i][j] = arr2[i][j]

"""

ans1 = Image.fromarray(ans.astype('uint8'))
ans1.save("ans.png")





