import numpy as np
import cv2
  
# Creating a black image with 3 
# channels RGB and unsigned int datatype 
img = np.zeros((800, 800, 3), dtype = "uint8") 
img.fill(255)

# Creating circle
cv2.circle(img, (400, 400), 80, (0, 0, 0), 2)

# Need to offset smaller circle by height of the arc which meets the larger circle
# R^2 - (x^2) = y^2. x = R/2 in this case

cv2.circle(img, (400, 480), 40, (255, 255, 255), -1)    # Remove part of larger circle, with size equal to what the smaller circle will have
cv2.circle(img, (400, 480), 40, (0, 0, 0), 2)           # Add smaller circle on the border of larger circle

cv2.ellipse(img, (400, 480), (40,40), 0, -10, 190, (255, 255, 255), 2)    # Use an "ellipse" (piece of circle in this case), to remove part of smaller circle

cv2.imshow('TITLE', img) 
  
# Allows us to see image 
# untill closed forcefully 
cv2.waitKey(0) 
cv2.destroyAllWindows() 