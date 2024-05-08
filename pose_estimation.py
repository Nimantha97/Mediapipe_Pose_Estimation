import base64
import cv2
import mediapipe as mp
import math
import matplotlib.pyplot as plt
from step_1 import *
from step_2 import *
from step_3 import *
from AllMethods import *
from io import BytesIO



# Initialize Mediapipe Pose class
mp_pose = mp.solutions.pose
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


#step 1
def estimate_step_1(img_file,  resize_width=640):
    input_img = cv2.imread(img_file)
    print(f"estimate_step_1 called with image path: {img_file}")
    output_img, landmarks = estimPose_img(input_img, display=False)  # Call the function to get output image and landmarks

    output_img = resize_image(output_img, resize_width)

    is_success, buffer = cv2.imencode(".png", output_img)
    if is_success:
        io_buf = BytesIO(buffer)
        encoded_image = base64.b64encode(io_buf.getvalue()).decode('utf-8')
    else:
        encoded_image = None


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

    # plt.imshow(output_img[:, :, ::-1])
    # plt.title("Step_1 Pose Analysis")
    # plt.axis('off')
    # plt.show()
    result_hip_and_ankle, message_hip_and_ankle = check_alignment_of_hip_and_ankle(left_hip, right_hip, left_knee,
                                                                                   right_knee, right_ankle, left_ankle)
    result_arms_down, message_arms_down = check_arms_down(left_hip, right_hip, left_shoulder, right_shoulder,
                                                          left_elbow, right_elbow)

    print(f"hip_and_ankle:  {message_hip_and_ankle}")
    print(f"arms_down:  {message_arms_down}")
    return encoded_image,message_hip_and_ankle, message_arms_down

def resize_image(image, target_width):
    height, width = image.shape[:2]
    aspect_ratio = width / height
    target_height = int(target_width / aspect_ratio)
    resized_image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)
    return resized_image

#step 2
def estimate_step_2(img_file, resize_width=640):
    input_img = cv2.imread(img_file)
    output_img, landmarks = estimPose_img(input_img,display=False)  # Call the function to get output image and landmarks

    output_img = resize_image(output_img, resize_width)

    is_success, buffer = cv2.imencode(".png", output_img)
    if is_success:
        io_buf = BytesIO(buffer)
        encoded_image = base64.b64encode(io_buf.getvalue()).decode('utf-8')
    else:
        encoded_image = None

    # left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    # right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
    # left_knee = landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value]
    # right_knee = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value]
    # left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    # right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    # left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    # right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    # left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
    # right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]

    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
    right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
    right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW]


    result_arms_ups, message_arms_ups = check_arms_ups(left_hip, right_hip, left_shoulder, right_shoulder, left_elbow,
                                                       right_elbow)
    result_hip_and_ankle, message_hip_and_ankle = check_alignment_of_hip_and_ankle(left_hip, right_hip, left_knee,
                                                                                   right_knee, right_ankle, left_ankle)

    print(f"hip_and_ankle: {result_hip_and_ankle}, {message_hip_and_ankle}")
    print(f"hands_up: {result_arms_ups}, {message_arms_ups}")

    #check fingers are locked

    image = cv2.imread(img_file)
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize MediaPipe hands solution
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)

    # Process the image and get the hand landmarks
    results = hands.process(image_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        # Iterate over each detected hand
        for hand_landmarks in results.multi_hand_landmarks:
            # Check finger lock status for each hand
            fingers_locked, fingers_locked_message = check_fingers_locked(hand_landmarks)
            print(fingers_locked_message)
            return encoded_image,fingers_locked_message,message_hip_and_ankle,message_arms_ups
    else:
        fingers_locked_message = "No fingers detected clearlty if you are not locked your fingers , please lock your all fingers while parms rotate upward"
        return encoded_image,fingers_locked_message,message_hip_and_ankle,message_arms_ups


#step 3
def estimate_step_3(img_file, resize_width=300):
    input_img = cv2.imread(img_file)
    output_img, landmarks = estimPose_img(input_img,
                                          display=False)  # Call the function to get output image and landmarks

    is_success, buffer = cv2.imencode(".png", output_img)
    if is_success:
        io_buf = BytesIO(buffer)
        encoded_image = base64.b64encode(io_buf.getvalue()).decode('utf-8')
    else:
        encoded_image = None


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
    right_foot_index = landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value]
    right_heel = landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value]
    result_arms_ups, message_arms_ups = check_arms_ups_right_side(left_hip, right_hip, left_shoulder, right_shoulder,
                                                        left_elbow, right_elbow)
    result_hip_and_ankle, message_hip_and_ankle = check_alignment_of_hip_and_ankle_right_side(left_hip, right_hip,left_knee, right_knee,right_ankle, left_ankle)

    image = cv2.imread(img_file)
    mp_pose1 = mp.solutions.pose.Pose()

    results = mp_pose1.process(image)
    if results.pose_landmarks:

        # plt.imshow(output_img[:, :, ::-1])
        # plt.title("Step_3 Pose Analysis")
        # plt.axis('off')
        # plt.show()

        is_standing_on_big_toes5,message_toe = is_standing_on_big_toes(results)
        message_toe1 = message_toe
        message_hip_and_ankle = message_hip_and_ankle
        message_arms_ups = message_arms_ups

        return encoded_image,message_toe1,message_hip_and_ankle,message_arms_ups
    else:

        message_toe1 = f"No toe landmarks detected"
        message_hip_and_ankle = message_hip_and_ankle
        message_arms_ups = message_arms_ups

    return encoded_image,message_toe1,message_hip_and_ankle,message_arms_ups


# step1_image = r'D:\project\Flask_app\images\step1.png'
# step2_image = r'D:\project\Flask_app\images\step2.png'
#step3_image = r'D:\project\Flask_app\images\step5.jpg'
#estimate_step_1(step1_image)
# estimate_step_2(step2_image)
#estimate_step_3(step3_image)
