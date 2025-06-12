import cv2
import pickle

# Load the image
image = cv2.imread("../src/carPark.png")

# Define top-left and bottom-right corners
pt1 = (40, 148)
pt2 = (147, 195)

# BGR color and thickness of lines
color = (255, 0, 255)
thickness = 2

# Width and Height of car parking spaces
width = pt2[0] - pt1[0]
height = pt2[1] - pt1[1]

# Try loading previously saved positions from the pickle file
try:
    with open("../output/carPark_pos.pickle", "rb") as file:
        pos_list = pickle.load(file)
except:
    pos_list = []

# Mouse click event handling
def mouseClicked(action, x, y, flags, *userdata):
    if action == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x, y))  # Add position on left-click

    if action == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x1, y1 = pos
            if (x1 < x < x1 + width) and (y1 < y < y1 + height):
                pos_list.pop(i)  # Remove rectangle on right-click

    # Save updated pos_list to a pickle file
    with open("../output/carPark_pos.pickle", "wb") as file:
        pickle.dump(pos_list, file)

while True:
    # Create a copy of the image each iteration
    image_copy = image.copy()

    # Set the mouse callback function for the window
    cv2.setMouseCallback("Car Park", mouseClicked)

    # Draw rectangles based on positions in pos_list
    for pos in pos_list:
        cv2.rectangle(image_copy, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), color, thickness)

    # Show the updated image
    cv2.imshow("Car Park", image_copy)

    # Wait for key press
    cv2.waitKey(1)
