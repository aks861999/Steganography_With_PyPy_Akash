# import the required modules #
import cv2
import numpy as np 
import random 

# Encryption function 
def encrypt(): 
      
    # img1 and img2 are the two input images 
    img1 = cv2.imread('path to the Image in which you want to hide') 
    img2 = cv2.imread('site.png') # Image File of the generated QR Code
      
    for i in range(img2.shape[0]): 
        for j in range(img2.shape[1]): 
            for l in range(3): 
                  
                # v1 and v2 are 8-bit pixel values 
                # of img1 and img2 respectively 
                v1 = format(img1[i][j][l], '08b') 
                v2 = format(img2[i][j][l], '08b') 
                  
                # Taking 4 MSBs of each image 
                v3 = v1[:4] + v2[:4]  
                  
                img1[i][j][l]= int(v3, 2) 
                  
    cv2.imwrite('output.png', img1) 
  
encrypt()
