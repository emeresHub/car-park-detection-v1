import cv2
import numpy as np
import pickle

# Load the positions from the pickle file
with open("./output/carPark_pos.pickle", "rb") as file:
    pos_list = pickle.load(file)

# Define dimensions for car park spaces
pt1 = (40, 148)  # Top-left corner
pt2 = (147, 195)  # Bottom-right corner

# BGR color and thickness of lines
color = (255, 0, 255)  # Purple color for the rectangle
thickness = 2  # Rectangle thickness

# Width and Height of car park spaces
width = pt2[0] - pt1[0]
height = pt2[1] - pt1[1]

# Initialize the video capture
cap = cv2.VideoCapture("src/carPark.mp4")

# Function to draw parking spaces
def get_parking_space(processed_image):
    occupied = len(pos_list)
    counter = 0
    for pos in pos_list:
        x, y = pos
        img_crop = processed_image[y:y+height, x:x+width]  # Crop the parking space
        # cv2.imshow(str(x * y), img_crop)  # Display the cropped parking space

        pixel_count = cv2.countNonZero(img_crop)

        font_scale = 0.5   # half size
        thickness  = 1     # thinner stroke
        text_pos = (x, y + height - 3)  # slightly above bottom edge
        #cv2.putText(img, str(pixel_count), text_pos, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness)

        if pixel_count < 800:
            color = (0,255,0)   # GREEN = free (few pixels)
            thickness = 3

        else:
            color = (0,0,255)   # RED   = occupied (many pixels)
            thickness = 3
            counter += 1


        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    # Label the free space / Total space
    cv2.putText(img, f"{occupied - counter}/{len(pos_list)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 6)


# Main loop for reading frames
while True:
    # Reset to the beginning of the video if the end is reached
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Read the frame
    ret, img = cap.read()

    # Convert to GrayScale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur (kernel size 3x3) with sigma valuem(standard deviation) spread (amount of blurr)
    blurr_image = cv2.GaussianBlur(gray_image,(3,3), 1)

    # Apply adaptive thresholding
    threshold_image = cv2.adaptiveThreshold(blurr_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)

    # Apply median blurr
    median_image = cv2.medianBlur(threshold_image, 5)

    # Dilate image to thicken lines
    kernel = kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    dilate_image = cv2.dilate(median_image, kernel, iterations=1)
    
    # Crop and display each parking space
    get_parking_space(dilate_image)

    if ret:
        # Show the frame with rectangles
        cv2.imshow("Car Park", img)
        # cv2.imshow("Gray Car Park", gray_image)
        # cv2.imshow("Blurr Car Park", blurr_image)
        # cv2.imshow("Threshold Image", threshold_image)
        # cv2.imshow("Median Image", threshold_image)
        # cv2.imshow("Dilated Image", dilate_image)

    # Wait for 1 ms before the next frame and exit when escape pressed
    if cv2.waitKey(1) & 0xFF == 27:  # press Esc to exit early
        break
