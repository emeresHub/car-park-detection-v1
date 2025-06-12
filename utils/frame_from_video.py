import cv2

# Load the video file
video = cv2.VideoCapture("../src/carPark.mp4")

# Set the required frame 
frame = 50
video.set(cv2.CAP_PROP_POS_FRAMES, frame)

# Extract the specified frame from video
ret, frame = video.read()

# Check video frame exists using ret bool logic, then save in a file
if ret:
    cv2.imwrite("../src/carPark.png", frame)

