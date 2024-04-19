import cv2
import mediapipe as mp

# Load the image
image = cv2.imread(r'D:\project\OpenCV_Yoga-Asanas-main\static\img\Warrior II pose.png')

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Convert the image to RGB (MediaPipe requires RGB input)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform pose estimation on the image
results = pose.process(image_rgb)

# Access pose landmarks if available
if results.pose_landmarks:
    # Access pose landmarks and perform further analysis
    pose_landmarks = results.pose_landmarks
    # Your analysis code here...

    # Visualize pose landmarks on the image (optional)
    for landmark in pose_landmarks.landmark:
        x = int(landmark.x * image.shape[1])
        y = int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

# Display the image with detected poses
cv2.imshow('Image with Poses', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
