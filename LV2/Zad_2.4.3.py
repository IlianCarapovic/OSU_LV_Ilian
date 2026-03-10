import numpy as np
import matplotlib.pyplot as plt

def enhance_brightness(image):
    bright_image = image + 100
    bright_image = np.clip(bright_image,0,255)
    return bright_image.astype(np.uint8)

def get_second_quarter(image):
    height, width = img.shape
    quarter_width = width//4
    quarter = image[:,2*quarter_width: 1*quarter_width:-1]
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

plt.subplot(2, 2, 1)
plt.imshow(enhance_brightness(img), cmap="gray")
plt.title("Enhanced Brightness")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(get_second_quarter(img), cmap="gray")
plt.title("Second Quarter")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(rotate_image90_right(img), cmap="gray")
plt.title("Rotated 90° Right")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(mirror_image(img), cmap="gray")
plt.title("Mirrored Image")
plt.axis("off")

plt.tight_layout()
plt.show()
