import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(r'D:\project\Flask_app\images\v5.mp4')

detector = pm.poseDetector()
# count = 0
# dir = 0
# pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1600,800))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        #detector.findAngle(img,28,30,32)
        #left Arm
        detector.findAngle(img,11,13,15)
        detector.findAngle(img, 12,14,16)


        detector.findAngle(img,23,25,27)
        detector.findAngle(img,24,26,28)
        detector.findAngle(img,24,12,14)
        detector.findAngle(img,23,11,13)
        #detector.findAngle(img,28,30,32)
        #detector.findAngle(img,27,29,31)


    cv2.imshow("Image", img)
    cv2.waitKey(1)


# import cv2
# import numpy as np
# import PoseModule as pm
#
# # Path to your image
# image_path = r"D:\project\Flask_app\images\standing_bigtoe.jpeg"  # Replace with your image path
#
# # Load the image
# img = cv2.imread(image_path)
#
# # Resize the image (optional)
# # img = cv2.resize(img, (1280, 720))  # Resize if needed
#
# # Create the pose detector object
# detector = pm.poseDetector()
#
# # Find pose landmarks on the image
# img = detector.findPose(img, draw=True)  # Set draw=True to display landmarks on image
#
# # Get the list of landmarks (if needed for further processing)
# lmList = detector.findPosition(img, draw=False)  # Set draw=False to skip drawing landmarks
#
# # Example: Find angle between right elbow, shoulder, and wrist
# detector.findAngle(img, 28, 30, 32)  # Adjust landmark indices as needed (refer to PoseModule)
#
# # Display the processed image
# cv2.imshow("Image", img)
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()  # Close all windows
