import numpy as np 
import matplotlib.pyplot as plt

# set to the amount of LEDs in your light strip
ledCount = 20 

# convert image to np array
imageArrRaw = plt.imread("testImg.jpg") 

# create subsections of the array for the LEDs
splitImageArr = np.array_split(imageArrRaw, ledCount)
averageColors = np.full((ledCount, 3), [0, 0, 0])

# create gradient
for i in range(0, len(splitImageArr)):
    imageShape = splitImageArr[i].shape
    newShape = (imageShape[0]*imageShape[1], imageShape[2])
    imageArrLin = np.reshape(splitImageArr[i], newShape)

    # mask red chanal 
    redMask = np.full(splitImageArr[i].shape, [0, 1, 1])
    redAverage = np.array(np.average(np.ma.array(imageArrLin, mask=redMask)))

    # mask green chanal 
    greenMask = np.full(splitImageArr[i].shape, [1, 0, 1])
    greenAverage = np.array(np.average(np.ma.array(imageArrLin, mask=greenMask)))

    # mask blue chanal 
    blueMask = np.full(splitImageArr[i].shape, [1, 1, 0])
    blueAverage = np.array(np.average(np.ma.array(imageArrLin, mask=blueMask)))

    # assignt RGB values to gradient
    averageColors[i][0] = redAverage
    averageColors[i][1] = greenAverage
    averageColors[i][2] = blueAverage

# show gradient
plt.imshow([averageColors])
plt.show()
