import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import math

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose
# Setting up the Pose model for images.
pose_img = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)

# Initializing mediapipe drawing class to draw landmarks on specified image.
mp_drawing = mp.solutions.drawing_utils


def estimPose_img(input_file, pose=pose_img, landmarks_c=(234, 63, 247), connection_c=(117, 249, 77),
                  thickness=2, circle_r=3, display=True):
    if isinstance(input_file, str):
        input_img = cv2.imread(input_file)
    else:
        input_img = input_file

    # Create a copy of the input image
    output_img = input_img.copy()

    # Convert the image from BGR into RGB format.
    RGB_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

    # Perform the Pose Detection.
    results = pose.process(RGB_img)

    # Retrieve the height and width of the input image.
    height, width, _ = input_img.shape

    # Initialize a list to store the detected landmarks.
    landmarks = []

    # Check if any landmarks are detected.
    if results.pose_landmarks:

        # Draw Pose landmarks on the output image.
        mp_drawing.draw_landmarks(output_img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(landmarks_c, thickness, circle_r),
                                  mp_drawing.DrawingSpec(connection_c, thickness, circle_r))

        # Iterate over the detected landmarks.
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x * width), int(landmark.y * height),
                              (landmark.z * width)))

    # Check if we want to display.
    if display:
        print("pose landmarks detected")
        # Display the original input image and the resulting image.
        plt.figure(figsize=[15, 15])
        plt.subplot(121)
        plt.imshow(input_img[:, :, ::-1])
        plt.title("Original image")
        plt.axis('off')
        plt.subplot(122)
        plt.imshow(output_img[:, :, ::-1])
        plt.title("Output image")
        plt.axis('off')

        # Plot the Pose landmarks in 3D.
        mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        # print(landmarks)

    # Just get output_img and landmarks
    else:
        # Return the output image and the found landmarks.

        return output_img, landmarks


def calculate_angle(point1, point2, point3):
    x1, y1, _ = point1
    x2, y2, _ = point2
    x3, y3, _ = point3
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    return angle


def check_tadasana_pose(img_file):
    """
    Estimates Tadasana pose angles and provides feedback.
    """

    # Get image and landmarks using estimPose_img
    output_img, landmarks = estimPose_img(img_file, display=False)

    # Define landmark indices for angle calculations
    ankle_knee_hip = (32, 28, 23)
    knee_hip_shoulder = (28, 23, 11)

    # Calculate and check ankle angle
    ankle_angle = calculate_angle(landmarks[ankle_knee_hip[0]], landmarks[ankle_knee_hip[1]],
                                  landmarks[ankle_knee_hip[2]])
    angle_threshold = 10  # Adjust threshold based on your needs
    if abs(ankle_angle - 180) > angle_threshold:
        print("Ankle angle incorrect: Adjust foot position (should be close to 180 degrees)")

    # Calculate and check knee angle
    knee_angle = calculate_angle(landmarks[knee_hip_shoulder[0]], landmarks[knee_hip_shoulder[1]],
                                 landmarks[knee_hip_shoulder[2]])
    if abs(knee_angle) > angle_threshold:
        print("Knee angle incorrect: Straighten legs with a slight microbend for stability")

    # You can add checks for other pose elements and desired angles here

    # Optional: Display the image with landmarks for visual feedback
    plt.imshow(output_img[:, :, ::-1])
    plt.title("Tadasana Pose Analysis")
    plt.axis('off')
    plt.show()

#
# # Example usage
# img_file = r'D:\project\Research_Development\images\p4.png'
# check_tadasana_pose(img_file)

# Provide paths to five images for each step
img_files = [
    r'D:\project\Research_Development\images\p1.jpg',
    r'D:\project\Research_Development\images\p2.jpg',
    r'D:\project\Research_Development\images\p3.jpg',
    r'D:\project\Research_Development\images\p4.jpg',
    r'D:\project\Research_Development\images\p5.jpg'
]


check_tadasana_pose(img_files[0])
check_tadasana_pose(img_files[1])
check_tadasana_pose(img_files[2])
check_tadasana_pose(img_files[3])
check_tadasana_pose(img_files[4])

""""
_, landmarks = estimPose_img(img_file, display=False)

print('The angle formed by',
      mp_pose.PoseLandmark(13).name, ',',
      mp_pose.PoseLandmark(11).name, 'and',
      mp_pose.PoseLandmark(23).name, 'is:',
      calculate_angle(landmarks[13], landmarks[11], landmarks[23]))

print('The angle formed by',
      mp_pose.PoseLandmark(11).name, ',',
      mp_pose.PoseLandmark(23).name, 'and',
      mp_pose.PoseLandmark(25).name, 'is:',
      calculate_angle(landmarks[11], landmarks[23], landmarks[25]))

print('The angle formed by',
      mp_pose.PoseLandmark(14).name, ',',
      mp_pose.PoseLandmark(12).name, 'and',
      mp_pose.PoseLandmark(24).name, 'is:',
      calculate_angle(landmarks[14], landmarks[12], landmarks[24]))

print('The angle formed by',
      mp_pose.PoseLandmark(12).name, ',',
      mp_pose.PoseLandmark(24).name, 'and',
      mp_pose.PoseLandmark(26).name, 'is:',
      calculate_angle(landmarks[12], landmarks[24], landmarks[26]))


--mediapose landmarks

  NOSE = 0
  LEFT_EYE_INNER = 1
  LEFT_EYE = 2
  LEFT_EYE_OUTER = 3
  RIGHT_EYE_INNER = 4
  RIGHT_EYE = 5
  RIGHT_EYE_OUTER = 6
  LEFT_EAR = 7
  RIGHT_EAR = 8
  MOUTH_LEFT = 9
  MOUTH_RIGHT = 10
  LEFT_SHOULDER = 11
  RIGHT_SHOULDER = 12
  LEFT_ELBOW = 13
  RIGHT_ELBOW = 14
  LEFT_WRIST = 15
  RIGHT_WRIST = 16
  LEFT_PINKY = 17
  RIGHT_PINKY = 18
  LEFT_INDEX = 19
  RIGHT_INDEX = 20
  LEFT_THUMB = 21
  RIGHT_THUMB = 22
  LEFT_HIP = 23
  RIGHT_HIP = 24
  LEFT_KNEE = 25
  RIGHT_KNEE = 26
  LEFT_ANKLE = 27
  RIGHT_ANKLE = 28
  LEFT_HEEL = 29
  RIGHT_HEEL = 30
  LEFT_FOOT_INDEX = 31
  RIGHT_FOOT_INDEX = 32

"""