# import cv2
# import mediapipe as mp
# import numpy as np
#
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
#
# # Define angle threshold (adjust based on your needs)
# angle_threshold = 10  # degrees
#
#
#
# # Define body landmark connections for angle calculation
# ankle_knee_hip = (32, 28, 23)
# knee_hip_shoulder = (28, 23, 11)
#
# def calculate_angle(landmark_list, landmark_indices):
#   # Get landmarks
#   landmark1 = landmark_list[landmark_indices[0]]
#   landmark2 = landmark_list[landmark_indices[1]]
#   landmark3 = landmark_list[landmark_indices[2]]
#
#   # Calculate vectors
#   v1 = np.array([landmark1.x, landmark1.y])
#   v2 = np.array([landmark2.x, landmark2.y])
#   v3 = np.array([landmark3.x, landmark3.y])
#
#   # Get angle in degrees
#   angle = np.degrees(np.arccos(((v1 - v2) * (v3 - v2)) / ((np.linalg.norm(v1 - v2) * np.linalg.norm(v3 - v2)))))
#   return angle
#
# def check_tadasana(landmarks):
#   # Check ankle angle (neutral, adjust threshold based on needs)
#   ankle_angle = calculate_angle(landmarks, ankle_knee_hip)
#   if abs(ankle_angle - 180) > angle_threshold:
#     print("Ankle angle incorrect: Adjust foot position (should be close to 180 degrees)")
#
#   # Check knee angle (straight with slight microbend)
#   knee_angle = calculate_angle(landmarks, knee_hip_shoulder)
#   # if abs(knee_angle) > angle_threshold:
#   #   print("Knee angle incorrect: Straighten legs with a slight microbend for stability")
#   if abs(knee_angle).any() > angle_threshold:
#     print("Ankle angle incorrect: Adjust foot position (should be close to 180 degrees)")
#
#   threshold_range = 10  # Adjust threshold range as needed
#   if not np.all(np.abs(knee_angle - 180) <= threshold_range):
#     print("Ankle angle incorrect: Adjust foot position (should be close to 180 degrees)")
#
#
# # Get user input image path
# image_path = (r'D:\project\Research_Development\images\p4.png')
#
# # Read image
# image = cv2.imread(image_path)
# if image is None:
#   print("Error: Could not read image from path.")
#   exit()
#
# # Convert image to RGB format
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# # Process image using MediaPipe Pose
# with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#   results = pose.process(image_rgb)
#
# # Draw pose landmarks on a copy of the image (optional)
# image_copy = image.copy()
# if results.pose_landmarks:
#   mp_drawing.draw_landmarks(image_copy, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#
# # Check body angles for Tadasana
# check_tadasana(results.pose_landmarks.landmark)
#
# # Display the image with or without landmarks (choose one)
# cv2.imshow('Tadasana Pose Analysis', image_copy)  # Display with landmarks (optional)
# # cv2.imshow('Tadasana Pose Analysis', image)  # Display without landmarks
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

#####################################################

import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Define angle threshold (adjust based on your needs)
angle_threshold = 10  # degrees

# Define body landmark connections for angle calculation
ankle_knee_hip = (32, 28, 23)
knee_hip_shoulder = (28, 23, 11)


def calculate_angle(landmark_list, landmark_indices):
    # Get landmarks
    landmark1 = landmark_list[landmark_indices[0]]
    landmark2 = landmark_list[landmark_indices[1]]
    landmark3 = landmark_list[landmark_indices[2]]

    # Calculate vectors
    v1 = np.array([landmark1.x, landmark1.y])
    v2 = np.array([landmark2.x, landmark2.y])
    v3 = np.array([landmark3.x, landmark3.y])

    # Get angle in degrees
    angle = np.degrees(np.arccos(((v1 - v2) * (v3 - v2)) / ((np.linalg.norm(v1 - v2) * np.linalg.norm(v3 - v2)))))
    return angle


def check_tadasana(landmarks):
    # Option 1: Assuming landmarks is a list of landmark objects
    # Check ankle angle (neutral, adjust threshold based on needs)
    ankle_angle = calculate_angle(landmarks, ankle_knee_hip)
    print(landmarks)
    print(ankle_angle)

    if abs(ankle_angle - 180).any() > angle_threshold:
        print("Ankle angle incorrect: Adjust foot position (should be close to 180 degrees)")

    # Check knee angle (straight with slight microbend)
    knee_angle = calculate_angle(landmarks, knee_hip_shoulder)
    # if abs(knee_angle) > angle_threshold:
    #   print("Knee angle incorrect: Straighten legs with a slight microbend for stability")
    if abs(knee_angle).any() > angle_threshold:
        print("Knee angle incorrect: Adjust foot position (should be close to 180 degrees)")

    threshold_range = 10  # Adjust threshold range as needed
    if not np.all(np.abs(knee_angle - 180) <= threshold_range):
        print("Knee angle incorrect: Adjust foot position (should be close to 180 degrees)")

    # Option 2: Assuming landmarks needs type casting to a list
    # landmarks = list(results.pose_landmarks)  # If landmarks is not already a list
    # ... (rest of the check_tadasana function)


# Get user input image path
image_path = r'D:\project\Research_Development\images\p6.png'

# Read image
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read image from path.")
    exit()

# Convert image to RGB format
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Process image using MediaPipe Pose
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    results = pose.process(image_rgb)

# Draw pose landmarks on a copy of the image (optional)
image_copy = image.copy()
if results.pose_landmarks:
    mp_drawing.draw_landmarks(image_copy, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

# Check body angles for Tadasana
check_tadasana(results.pose_landmarks.landmark)

# Display the image with or without landmarks (choose one)
cv2.imshow('Tadasana Pose Analysis', image_copy)  # Display with landmarks (optional)
cv2.imshow('Tadasana Pose Analysis', image)  # Display without landmarks
cv2.waitKey(0)
cv2.destroyAllWindows()
