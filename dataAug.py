# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:44:09 2022

@author: saideni
"""


# importing all the required libraries
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import skimage.io as io
from skimage.transform import rotate, AffineTransform, warp
from skimage.util import random_noise
from skimage.filters import gaussian
#import matplotlib.pyplot as plt



def dataAugmentation(Path):
    image = io.imread(Path)
    print(image.shape)
    rotated45 = rotate(image, angle=45, mode = 'wrap')
    rotated90 = rotate(image, angle=90, mode = 'wrap')
    rotatedn90 = rotate(image, angle=-90, mode = 'wrap')
    transform = AffineTransform(translation=(25,25))
    wrapShift = warp(image,transform,mode='wrap')
    flipLR = np.fliplr(image)
    flipUD = np.flipud(image)
    sigmaList = [0.155, 0.2, 0.3, 0.4]
    noisyImages = []
    #add random noise to the image
    for i in sigmaList:
        noisyRandom = random_noise(image,var=i**2)
        noisyImages.append(noisyRandom)
    
    blurred = gaussian(image,sigma=10,multichannel=True)

    
    
    io.imsave('rotated45.jpg',rotated45)
    io.imsave('rotated90.jpg',rotated90)
    io.imsave('rotatedn90.jpg',rotatedn90)
    io.imsave('wrapShift.jpg',wrapShift)
    io.imsave('flipLR.jpg',flipLR)
    io.imsave('flipUD.jpg',flipUD)
    io.imsave('noisyImages0155.jpg',noisyImages[0])
    io.imsave('noisyImages0200.jpg',noisyImages[1])
    io.imsave('noisyImages0300.jpg',noisyImages[2])
    io.imsave('noisyImages0400.jpg',noisyImages[3])
    io.imsave('blurred.jpg',blurred)
    return image, rotated45, rotated90, rotatedn90, wrapShift, flipLR, flipUD, noisyImages, blurred

res = dataAugmentation('wael.jpg')
