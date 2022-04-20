# import imageio as iio #Tried these, they all either fail or not do what I intended
# import visvis as vv  # Might need to
# from PIL import Image
import cv2
import math

import numpy as np


demo_arr = np.random.randint(1,9, size = (4,6,3))
print(demo_arr[0,2,1])

#endregion




# img = iio.imread("J&E_Abby_Wedding.jpg")
# vv.imshow(img)

img = cv2.imread("J&E_Abby_Wedding.jpg")
img = cv2.imread("J&E_Saint_L.jpg")
img = cv2.imread("J&E_With_Vicky.jpg")


#set up dummy to show I can get the mean average of a designated blotch
img2 = img.copy()                               # copy the imgage so the original is unedited
LargePix = img2[120:240, 120:240, :]            # designate space we want to mean Red Green and Blue (3 averages)
mean_pix = LargePix.mean(axis = (0,1)).round()  # get means of row and column then round
# LargePix[:,:] = mean_pix                      # unused to normally set the mean color to LargePix

img2[120:240, 120:240] = mean_pix               # replace all pixels in the originally chosen space with the mean RGB

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', pic.img)
# cv2.resizeWindow('image', width = 1000, height=1000)
cv2.waitKey(0)  # show window until key press
cv2.destroyAllWindows()  # then destroy

#alternative way of indexing
rows = np.arange(0,120)
columns = np.arange(0,120)
img2[np.ix_(rows,columns)]

# largePix = img_trans[
#            y_dice * blockLen: (y_dice + 1) * blockLen,
#            x_dice * blockLen: (x_dice + 1) * blockLen,
#            :]
#input image to show whatever here
show_im(LargePix)
show_im(img2)
possible_blocks(1080, 1920) # these should eventually changed to just input a picture and it auto extracts the size