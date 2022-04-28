import Dice_Picture

from importlib import reload
Dice_Picture = reload(Dice_Picture)

image = "J&E_Abby_Wedding.jpg"
image = "J&E_Saint_L.jpg"
image = "J&E_With_Vicky.jpg"
image = "J&E_Sunshine.jpg"


pic = Dice_Picture.dicePic(image)
# pic = Dice_Picture.dicePic(image, crop=[1620,2040])
pic = Dice_Picture.dicePic(image, crop=[2800,2300])

# pic.possible_blocks()  #for showing possible blocks but this is already called from init

# pic.dice_alt([36,64])
pic.dice_alt(pic.posDiceNum[6])


pic.showIm()                      # show original picture
pic.showIm(image=pic.img_trans)   #show translated image that is original size
pic.showIm(image=pic.img_reduced) #show trans picture but in single pixel blocks for easier display
# pic.showIm()

############### beta testing ###################
#for getting those dice strips
image2 = "Dice_strips/p_strip.jpg"
image2 = "Austor 100 piece (square).jpg"

pic2 = Dice_Picture.dicePic(image2)


# Black
dice_black = np.array([40, 40, 40])

# brown
dice_brown = np.array([155, 60, 40])

# red
dice_red = np.array([200, 30, 30])

# Orange
dice_orange = np.array([250, 102, 70])

# Green
dice_green = np.array([58, 170, 151])

# Blue
dice_blue= np.array([40, 110, 245])

# Light Purple
dice_Lpurple= np.array([200, 160, 200])

# Dark Purple
dice_Dpurple = np.array([67, 27, 107])

# White
dice_white = np.array([230, 230, 250])

#{'dice_black':{0:np.array([40, 40, 40]), 1:np.array([45, 45, 45])}
dice_dict = {}
dice_dict = {'dice_black':np.array([40, 40, 40]),
            'dice_brown':np.array([155, 60, 40]),
            'dice_red':np.array([200, 30, 30]),
            'dice_orange':np.array([250, 102, 70]),
            'dice_green':np.array([58, 170, 151]),
            'dice_blue':np.array([40, 110, 245]),
            'dice_Lpurple':np.array([200, 160, 200]),
            'dice_Dpurple':np.array([67, 27, 107]),
            'dice_white':np.array([230, 230, 250])
}


centroids = []
for key, value in dice_dict.items():
    centroids.append(value)

points = np.array(np.random.randint(250, size=(20, 3)))
points


from scipy.spatial import distance

pw_dist = distance.cdist(points, centroids)
pw_dist

labels = np.argmin(pw_dist, axis =1) # get min column ndx per row
labels #The index is the centroid's index that is closest to the point

centroids = np.array(centroids)
centroids[labels]





mean_centroids = np.mean(centroids, axis = 1)
mean_centroids

mean_points =  np.mean(points, axis = 1)
mean_points

pseudo_lables = []
lowest_number = 251
lowest_cent = -1
for i in range(0, len(mean_points)):
    for ii in range(0, len(mean_centroids)):
        compNum = abs(mean_points[i] - mean_centroids[ii])
        if compNum < lowest_number:
            lowest_number = compNum
            lowest_cent = ii
    pseudo_lables.append(lowest_cent)


