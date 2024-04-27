import cv2
import mediapipe as mp
import math

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    angle = math.degrees(radians)
    if angle < 0:
        angle += 360
    return angle

# Function to check alignment of feet
def check_alignment_of_feet(left_ankle, right_ankle):
    angle_between_feet = abs(left_ankle[0] - right_ankle[0])
    # Check if feet are aligned
    if angle_between_feet < 20:
        return True, "Feet aligned correctly"
    else:
        return False, "Feet not aligned correctly"

# Function to check engagement of thigh muscles
def check_engagement_of_thigh_muscles(left_hip, right_hip, left_knee, right_knee):
    angle_left_thigh = calculate_angle(left_hip, left_knee, (left_knee[0], left_knee[1]+1))
    angle_right_thigh = calculate_angle(right_hip, right_knee, (right_knee[0], right_knee[1]+1))
    # Check if thigh muscles are engaged
    if 160 < angle_left_thigh < 200 and 160 < angle_right_thigh < 200:
        return True, "Thigh muscles engaged correctly"
    else:
        return False, "Thigh muscles not engaged correctly"

# Function to check pelvic alignment
def check_pelvic_alignment(left_hip, right_hip, left_shoulder, right_shoulder):
    angle_left_pelvis = calculate_angle(left_hip, left_shoulder, (left_shoulder[0], left_shoulder[1]-1))
    angle_right_pelvis = calculate_angle(right_hip, right_shoulder, (right_shoulder[0], right_shoulder[1]-1))
    # Check if pelvis is aligned
    if 170 < angle_left_pelvis < 190 and 170 < angle_right_pelvis < 190:
        return True, "Pelvis aligned correctly"
    else:
        return False, "Pelvis not aligned correctly"

# Function to check shoulder alignment
def check_shoulder_alignment(left_shoulder, right_shoulder, left_elbow, right_elbow):
    angle_left_shoulder = calculate_angle(left_shoulder, left_elbow, (left_elbow[0], left_elbow[1]-1))
    angle_right_shoulder = calculate_angle(right_shoulder, right_elbow, (right_elbow[0], right_elbow[1]-1))
    # Check if shoulders are aligned
    if 80 < angle_left_shoulder < 100 and 80 < angle_right_shoulder < 100:
        return True, "Shoulders aligned correctly"
    else:
        return False, "Shoulders not aligned correctly"

# Function to check arm position
def check_arm_position(left_shoulder, right_shoulder, left_elbow, right_elbow):
    angle_left_arm = calculate_angle(left_shoulder, left_elbow, (left_shoulder[0], left_shoulder[1]+1))
    angle_right_arm = calculate_angle(right_shoulder, right_elbow, (right_shoulder[0], right_shoulder[1]+1))
    # Check if arms are in correct position
    if 80 < angle_left_arm < 100 and 80 < angle_right_arm < 100:
        return True, "Arms in correct position"
    else:
        return False, "Arms not in correct position"


# Example usage for each step of Tadasana pose
def estimate_tadasana_pose_steps():
    # Initialize Mediapipe Pose class
    mp_pose = mp.solutions.pose
    pose_img = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)

    # Provide paths to five images for each step
    img_files = [
        r'D:\project\Research_Development\images\p1.jpg',
        r'D:\project\Research_Development\images\p2.jpg',
        r'D:\project\Research_Development\images\p3.jpg',
        r'D:\project\Research_Development\images\p4.jpg',
        r'D:\project\Research_Development\images\p5.jpg'
    ]

    # Iterate over each image
    for i, img_file in enumerate(img_files, start=1):
        # Get image and landmarks
        input_img = cv2.imread(img_file)
        output_img = input_img.copy()
        RGB_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
        results = pose_img.process(RGB_img)
        height, width, _ = input_img.shape
        landmarks = []

        # Draw landmarks on the output image
        if results.pose_landmarks:
            for landmark in results.pose_landmarks.landmark:
                landmarks.append((int(landmark.x * width), int(landmark.y * height), (landmark.z * width)))

        # Check each pose step
        left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
        right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
        left_knee = landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value]
        right_knee = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]

        if i == 1:
            result, message = check_alignment_of_feet(left_ankle, right_ankle)
        elif i == 2:
            result, message = check_engagement_of_thigh_muscles(left_hip, right_hip, left_knee, right_knee)
        elif i == 3:
            result, message = check_pelvic_alignment(left_hip, right_hip, left_shoulder, right_shoulder)
        elif i == 4:
            result, message = check_shoulder_alignment(left_shoulder, right_shoulder, left_elbow, right_elbow)
        elif i == 5:
            result, message = check_arm_position(left_shoulder, right_shoulder, left_elbow, right_elbow)

        print(f"Step {i}: {message}")

# Call the function
estimate_tadasana_pose_steps()
