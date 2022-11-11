import PySimpleGUI as sg
import cv2
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("See Pencil Sketch")]]

###Building Window
window = sg.Window('Pencil Sketch', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "See Pencil Sketch":
        #print(values["-IN-"])
        img = values["-IN-"]
        img = cv2.imread(img)

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