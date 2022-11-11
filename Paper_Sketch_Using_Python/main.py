import cv2

#*if wanted to ask user to input there own photo*
#IMAGE_NAME = (input("Enter image file name and extension: "))
#IMAGE_LOCATION = input("Enter img location (i.e. C:/Users/Tico/Desktop/) ")
#img_location = IMAGE_LOCATION
#filename = IMAGE_NAME



#location of the image 

#img_location = 'C:/Users/Tico/Desktop/'
img_location = 'C:/Users/rjrus/Downloads/'

#file name for the image with extension
filename = 'mushroom.jfif'

#read in the image
img = cv2.imread(img_location+filename)

#convert img to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#invert img
inverted_gray_image = 255 - gray_image

#blur image by gaussians function
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

#invert the blurred img
inverted_blurred_img = 255 - blurred_img

#create pencil sketch
pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)


cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_img)

cv2.waitKey(0)