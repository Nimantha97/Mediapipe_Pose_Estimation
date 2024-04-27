import cv2
import mediapipe as mp
import math
import matplotlib.pyplot as plt

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose
# Setting up the Pose model for images.
pose_img = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)

# Initializing mediapipe drawing class to draw landmarks on specified image.
mp_drawing = mp.solutions.drawing_utils


# # Function to calculate angle between three points
# def calculate_angle(a, b, c):
#     radians = math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
#     angle = math.degrees(radians)
#     if angle < 0:
#         angle += 360
#     return angle


def normalize_landmark(landmark, image_shape):
  """Normalizes landmark coordinates based on image dimensions."""
  x, y = landmark
  return x / image_shape[1], y / image_shape[0]  # Normalize to 0-1 range

def calculate_angle(landmark1, landmark2, landmark3, image_shape):
  """Calculates the angle between three normalized landmarks."""
  normalized_landmarks = [normalize_landmark(lm, image_shape) for lm in [landmark1, landmark2, landmark3]]
  v1, v2 = map(lambda p1, p2: (p2[0] - p1[0], p2[1] - p1[1]), normalized_landmarks[:2], normalized_landmarks[1:])
  angle = math.degrees(math.atan2(v2[1], v2[0]))
  return (angle + 360) % 360  # Wrap angle to 0-360 degrees

# Function to check alignment of feet (with relaxed threshold)
def check_alignment_of_feet(left_ankle, right_ankle, image_shape):
  angle_between_feet = abs(normalize_landmark(left_ankle, image_shape)[0] - normalize_landmark(right_ankle, image_shape)[0]) * image_shape[1]
  # Relaxed threshold for foot alignment (10-20 degrees)
  if 10 <= angle_between_feet <= 20:
    return True, "Feet aligned correctly"
  else:
    feedback_message = "Feet are not hip-width apart. "
    if angle_between_feet < 10:
      feedback_message += "Try bringing your feet slightly further apart."
    else:
      feedback_message += "Try bringing your feet closer together."
    return False, feedback_message

# Function to check engagement of thigh muscles (with wider range and alternative feedback)
def check_engagement_of_thigh_muscles(left_hip, right_hip, left_knee, right_knee, image_shape):
  angle_left_thigh = calculate_angle(left_hip, left_knee, (left_knee[0], left_knee[1] + 1))
  angle_right_thigh = calculate_angle(right_hip, right_knee, (right_knee[0], right_knee[1] + 1))
  # Relaxed threshold for thigh engagement (150-210 degrees)
  if 150 <= angle_left_thigh <= 210 and 150 <= angle_right_thigh <= 210:
    return True, "Thigh muscles engaged correctly"
  else:
    feedback_message = "Thigh muscles not engaged correctly. "
    if angle_left_thigh < 150 and angle_right_thigh < 150:
      feedback_message += "Focus on straightening your legs slightly more to engage your thighs."
    elif angle_left_thigh > 210 and angle_right_thigh > 210:
      feedback_message += "Your knees might be hyperextended. Maintain a slight bend in your knees."
    else:
      feedback_message += "Try adjusting your leg position to achieve a straighter posture."
    return False, feedback_message

# Function to check pelvic alignment (with refined feedback)
def check_pelvic_alignment(left_hip, right_hip, left_shoulder, right_shoulder, image_shape):
  angle_left_pelvis = calculate_angle(left_hip, left_shoulder, (left_shoulder[0], left_shoulder[1] - 1))
  angle_right_pelvis = calculate_angle(right_hip, right_shoulder, (right_shoulder[0], right_shoulder[1] - 1))
  # Maintain threshold for pelvic alignment (170-190 degrees)
  if 170 <= angle_left_pelvis <= 190 and 170 <= angle_right_pelvis <= 190:
    return True, "Pelvis aligned correctly"
  else:
    feedback_message = "Pelvis not aligned correctly. "
    if angle_left_pelvis < 170 and angle_right_pelvis < 170:
      feedback_message += "Try tucking your tailbone slightly under to maintain a neutral"
      return False, feedback_message


# Function to check shoulder alignment (with wider range and alternative feedback)
def check_shoulder_alignment(left_shoulder, right_shoulder, left_elbow, right_elbow, image_shape):
  angle_left_shoulder = calculate_angle(left_shoulder, left_elbow, (left_shoulder[0], left_shoulder[1] - 1))
  angle_right_shoulder = calculate_angle(right_shoulder, right_elbow, (right_shoulder[0], right_shoulder[1] - 1))
  # Relaxed threshold for shoulder alignment (70-110 degrees)
  if 70 <= angle_left_shoulder <= 110 and 70 <= angle_right_shoulder <= 110:
    return True, "Shoulders aligned correctly"
  else:
    feedback_message = "Shoulders not aligned correctly. "
    if angle_left_shoulder < 70 and angle_right_shoulder < 70:
      feedback_message += "Try rolling your shoulders back and down to open your chest."
    elif angle_left_shoulder > 110 and angle_right_shoulder > 110:
      feedback_message += "Your shoulders might be rounded forward. Relax your shoulders and maintain an open chest posture."
    else:
      feedback_message += "Try adjusting your arm position to achieve a more neutral shoulder alignment."
    return False, feedback_message

# Function to check arm position (with relaxed threshold)
def check_arm_position(left_shoulder, right_shoulder, left_elbow, right_elbow, image_shape):
  angle_left_arm = calculate_angle(left_shoulder, left_elbow, (left_shoulder[0], left_shoulder[1] + 1))
  angle_right_arm = calculate_angle(right_shoulder, right_elbow, (right_shoulder[0], right_shoulder[1] + 1))
  # Relaxed threshold for arm position (70-110 degrees)
  if 70 <= angle_left_arm <= 110 and 70 <= angle_right_arm <= 110:
    return True, "Arms in correct position"
  else:
    feedback_message = "Arms not in correct position. "
    if angle_left_arm < 70 and angle_right_arm < 70:
      feedback_message += "Try extending your arms slightly further away from your body."
    elif angle_left_arm > 110 and angle_right_arm > 110:
      feedback_message += "Your arms might be bent too much. Straighten your arms slightly while maintaining a slight bend at the elbows."
    else:
      feedback_message += "Try adjusting your arm position to achieve a straighter posture with a slight elbow bend."
    return False, feedback_message



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



#cheking tadasana steps
def check_tadasana_step(img_file, step_num, display=False):
    # Get image and landmarks
    input_img = cv2.imread(img_file)
    output_img, landmarks = estimPose_img(input_img, display=False)  # Call the function to get output image and landmarks

    # Check pose step based on step_num (using a dictionary for step checks)
    step_check_functions = {
        1: (check_alignment_of_feet, "Feet should be hip-width apart. Adjust your feet position."),
        2: (check_engagement_of_thigh_muscles, "Engage your thigh muscles by straightening your legs slightly. Knees should be over your ankles."),
        3: (check_pelvic_alignment, "Maintain a neutral pelvic tilt. Avoid tilting your pelvis forward or backward."),
        4: (check_shoulder_alignment, "Roll your shoulders back and down to open your chest. Shoulders should be in line with your hips."),
        5: (check_arm_position, "Extend your arms parallel to the sides of your body. Elbows should be slightly bent."),
    }

    if step_num in step_check_functions:
        result, message = step_check_functions[step_num]

        if not result:
            # Provide specific feedback based on the step check function's message
            feedback_message = {
                "Feet not aligned correctly": "Try bringing your feet closer together to achieve hip-width apart.",
                "Thigh muscles not engaged correctly": "Focus on straightening your legs slightly to engage your thighs. Knees should be aligned over your ankles.",
                "Pelvis not aligned correctly": "Maintain a neutral pelvic tilt by avoiding tilting your pelvis forward or backward.",
                "Shoulders not aligned correctly": "Roll your shoulders back and down to open your chest. Aim for your shoulders to be in line with your hips.",
                "Arms not in correct position": "Extend your arms parallel to the sides of your body. Elbows should have a slight bend.",
            }.get(message, message)  # Use default message if not found
            return result, feedback_message
        else:
            return result, message  # Step passed, return original message
    else:
        print(f"Invalid step number: {step_num}")
        return False, "Invalid step"


image_file = r'D:\project\Research_Development\images\t1.png'
step_num = 1
step_check_functions = {1,2,3,4,5}
result = check_tadasana_step(image_file, step_num, display=False)
print(result)


# step_num = 1
# step_check_functions = {1: check_tadasana_step}
# result = check_tadasana_step(image_file, step_num, display=False)


#
#
# img_files = [
#     r'D:\project\Research_Development\images\t1.png',
#     r'D:\project\Research_Development\images\legs-1.jpg',
#     r'D:\project\Research_Development\images\hand and leg-2.jpg',
#     r'D:\project\Research_Development\images\legs and hand 2-3.jpg',
#     r'D:\project\Research_Development\images\legs and hand-4.jpg',
#     r'D:\project\Research_Development\images\standing-5.jpg'
# ]
#
# # Loop through each image file
# for img_file in img_files:
#     # Step number to check (replace with the desired step number)
#     step_num = 1  # Change this to the specific step you want to check
#
#     # Call the check_tadasana_step function
#     #result, message = check_tadasana_step(img_file, [step_num], display=True)
#     result = check_tadasana_step(img_file, step_num, display=True)
#
#
#
#     # Print the results
#     print(f"Image: {img_file}")
#     if result:
#         print(f"Step {step_num} passed: {feedback_message}")
#     else:
#         print(f"Step {step_num} failed: {message}")
#
#
#
