import cv2
import numpy as np

def create_image(img_shape, bgr_value):
    # create a blank_img
    blank_img = np.zeros(img_shape, np.uint8)

    # fill bgr values in blank_img to give required background
    blank_img[:] = bgr_value
    return blank_img

def alpha_blending():
    '''
    ALPHA BLENDING:-
    result = (a * F) + ( (1 - a) * B)
    result => resultant image
    F => Foreground image
    B => Background image
    a => Alpha matte/mask
    ''' 

    # Read given images
    foreground = cv2.imread("input.jpg")
    alpha = cv2.imread("mask.png")

    # create red background image
    # with same shape of foreground image
    red_background = create_image(foreground.shape, (0, 0, 255))


    # resize alpha matte to the dimensions of foreground image
    # this step is neccessary to perform multiplication
    dimensions = tuple(reversed(foreground.shape[:2]))
    alpha = cv2.resize(alpha, dimensions)

    
    # Convert datatype from uint8 to float
    foreground = foreground.astype(float)
    red_background = red_background.astype(float)
    
    # Normalize the alpha mask 
    # this step is neccessary to keep intensity between 0 and 1
    alpha = alpha.astype(float)/255
    
    # Multiply the foreground with the alpha matte
    foreground = cv2.multiply(alpha, foreground)
    
    # Multiply the background with ( 1 - alpha )
    red_background = cv2.multiply(1.0 - alpha, red_background)
    
    # Add the masked foreground and background.
    outImage = cv2.add(foreground, red_background)
    
    # Save image
    cv2.imwrite("outImg.jpg", outImage)


if __name__ == "__main__":
    alpha_blending()

