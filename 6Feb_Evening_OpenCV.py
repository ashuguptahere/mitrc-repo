import cv2
camera = cv2.VideoCapture(0)
for i in range(1):
    return_value, image = camera.read()
    cv2.imwrite('C:/Users/fluXcapacit0r/Desktop/opencv'+
                str(i)+'.png', image)
del(camera)

# importing pyplot and image from matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
# reading png image file 
im = img.imread(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\javk.jpg") 
# show image 
plt.imshow(im) 

# importing pyplot and image from matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
# reading png image 
im = img.imread(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\javk.jpg")  
# applying pseudocolor  
# default value of colormap is used. 
lum = im[:, :, 0] 
# show image 
plt.imshow(lum) 


# importing pyplot and image from matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
  
# reading png image 
im = img.imread(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\javk.jpg") 
lum = im[:, :, 0] 
  
# setting colormap as hot 
plt.imshow(lum, cmap ='hot') 
plt.colorbar() 

############################################
# importing PIL and matplotlib 
from PIL import Image 
import matplotlib.pyplot as plt 

# reading png image file 
img = Image.open(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\javk.jpg") 

# resizing the image 
img.thumbnail((50, 50), Image.ANTIALIAS) 
imgplot = plt.imshow(img) 

