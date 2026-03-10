import numpy as np
import matplotlib.pyplot as plt

def enhance_brightness(image):
    return image + 100

def get_second_quarter(image):
    height, width = img.shape
    quarter_width = width//4
    quarter = image[:,1*quarter_width: 2*quarter_width]
    return quarter

def rotate_image90_right(image):
    return np.rot90(image,3)

def mirror_image(image):
    #Left right mirroring
    #Also we can use image[:,::-1] LR or fliplr()
    #also we can use image[::-1,:] UP DOWN or flipud
    return np.fliplr(image)


#returns a numpy array
#[height,with,channels]
img = plt.imread("road.jpg")
#matrix indexing [row,colum,chanel]
img = img[:,:,0].copy()

print(img.shape)
print(img.dtype)

plt.figure()
#plt.imshow(enhance_brightness(img), cmap="gray")
#plt.imshow(get_second_quarter(img), cmap="gray")
#plt.imshow(rotate_image90_right(img), cmap="gray")
plt.imshow(mirror_image(img), cmap="gray")

plt.show()