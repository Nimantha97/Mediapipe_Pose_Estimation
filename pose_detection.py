# required libraries
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import math


# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose
# Setting up the Pose model for images.
pose_img = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)
# Setting up the Pose model for videos.
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5,
                          min_tracking_confidence=0.5, model_complexity=1)

# Initializing mediapipe drawing class to draw landmarks on specified image.
mp_drawing = mp.solutions.drawing_utils


def estimPose_img(input_file, pose=pose_img, landmarks_c=(234, 63, 247), connection_c=(117, 249, 77),
                  thickness=2, circle_r=3, display=True):
    # Read the input image
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
        plt.subplot(121);
        plt.imshow(input_img[:, :, ::-1]);
        plt.title("Original image");
        plt.axis('off');
        plt.subplot(122);
        plt.imshow(output_img[:, :, ::-1]);
        plt.title("Output image");
        plt.axis('off');

        # Plot the Pose landmarks in 3D.
        mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        #print(landmarks)

    # Just get output_img and landmarks
    else:
        # Return the output image and the found landmarks.

        return output_img, landmarks


img_file = r'D:\project\Research_Development\images\p3.png'
#estimPose_img(r'D:\project\OpenCV_Yoga-Asanas-main\static\img\Warrior II pose.png')
estimPose_img(img_file)


#######################################

# Calculate the angle between three points
def calcul_angle(point1, point2, point3):
    x1, y1, _ = point1
    x2, y2, _ = point2
    x3, y3, _ = point3
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    return angle


_, landmarks = estimPose_img(img_file, display=False)

print('The angle formed by',
      mp_pose.PoseLandmark(13).name, ',',
      mp_pose.PoseLandmark(11).name, 'and',
      mp_pose.PoseLandmark(23).name, 'is:',
      calcul_angle(landmarks[13], landmarks[11], landmarks[23]))

print('The angle formed by',
      mp_pose.PoseLandmark(11).name, ',',
      mp_pose.PoseLandmark(23).name, 'and',
      mp_pose.PoseLandmark(25).name, 'is:',
      calcul_angle(landmarks[11], landmarks[23], landmarks[25]))

print('The angle formed by',
      mp_pose.PoseLandmark(14).name, ',',
      mp_pose.PoseLandmark(12).name, 'and',
      mp_pose.PoseLandmark(24).name, 'is:',
      calcul_angle(landmarks[14], landmarks[12], landmarks[24]))

print('The angle formed by',
      mp_pose.PoseLandmark(12).name, ',',
      mp_pose.PoseLandmark(24).name, 'and',
      mp_pose.PoseLandmark(26).name, 'is:',
      calcul_angle(landmarks[12], landmarks[24], landmarks[26]))