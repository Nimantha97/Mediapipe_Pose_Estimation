# import cv2
# import mediapipe as mp
# import math
# import matplotlib.pyplot as plt
# import step_1 as s1
# import AllMethods as cal
#
#
# # Initializing mediapipe pose class.
# mp_pose = mp.solutions.pose
# # Setting up the Pose model for images.
# pose_img = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)
#
# # Initializing mediapipe drawing class to draw landmarks on specified image.
# mp_drawing = mp.solutions.drawing_utils
#
# cal_angle = cal.CalculateAngle()
#
#
#
# # Function to calculate angle between three points
# def calculate_angle(a, b, c):
#     radians = math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
#     angle = math.degrees(radians)
#     if angle < 0:
#         angle += 360
#     return angle
#
#
# # Function to check alignment of feet
# # def check_alignment_of_feet(left_ankle, right_ankle):
# #     angle_between_feet = abs(left_ankle[0] - right_ankle[0])
# #     # Check if feet are aligned
# #     if angle_between_feet < 20:
# #         return True, "Feet aligned correctly"
# #     else:
# #         return False, "Feet not aligned correctly"
# #
# #
# # # Function to check engagement of thigh muscles
# # def check_engagement_of_thigh_muscles(left_hip, right_hip, left_knee, right_knee):
# #     angle_left_thigh = calculate_angle(left_hip, left_knee, (left_knee[0], left_knee[1] + 1))
# #     angle_right_thigh = calculate_angle(right_hip, right_knee, (right_knee[0], right_knee[1] + 1))
# #     # Check if thigh muscles are engaged
# #     if 160 < angle_left_thigh < 200 and 160 < angle_right_thigh < 200:
# #         return True, "Thigh muscles engaged correctly"
# #     else:
# #         return False, "Thigh muscles not engaged correctly"
# #
# #
# # # Function to check pelvic alignment
# # def check_pelvic_alignment(left_hip, right_hip, left_shoulder, right_shoulder):
# #     angle_left_pelvis = calculate_angle(left_hip, left_shoulder, (left_shoulder[0], left_shoulder[1] - 1))
# #     angle_right_pelvis = calculate_angle(right_hip, right_shoulder, (right_shoulder[0], right_shoulder[1] - 1))
# #     # Check if pelvis is aligned
# #     if 170 < angle_left_pelvis < 190 and 170 < angle_right_pelvis < 190:
# #         return True, "Pelvis aligned correctly"
# #     else:
# #         return False, "Pelvis not aligned correctly"
# #
# #
# # # Function to check shoulder alignment
# # def check_shoulder_alignment(left_shoulder, right_shoulder, left_elbow, right_elbow):
# #     angle_left_shoulder = calculate_angle(left_shoulder, left_elbow, (left_elbow[0], left_elbow[1] - 1))
# #     angle_right_shoulder = calculate_angle(right_shoulder, right_elbow, (right_elbow[0], right_elbow[1] - 1))
# #     # Check if shoulders are aligned
# #     if 80 < angle_left_shoulder < 100 and 80 < angle_right_shoulder < 100:
# #         return True, "Shoulders aligned correctly"
# #     else:
# #         return False, "Shoulders not aligned correctly"
# #
# #
# # # Function to check arm position
# # def check_arm_position(left_shoulder, right_shoulder, left_elbow, right_elbow):
# #     angle_left_arm = calculate_angle(left_shoulder, left_elbow, (left_shoulder[0], left_shoulder[1] + 1))
# #     angle_right_arm = calculate_angle(right_shoulder, right_elbow, (right_shoulder[0], right_shoulder[1] + 1))
# #     # Check if arms are in correct position
# #     if 80 < angle_left_arm < 100 and 80 < angle_right_arm < 100:
# #         return True, "Arms in correct position"
# #     else:
# #         return False, "Arms not in correct position"
# #
# ######################### working####
#
# # Fnction to check alignment of feet step 1u
# # def check_alignment_of_feet(left_ankle, right_ankle):
# #     angle_between_feet = abs(left_ankle[0] - right_ankle[0])
# #     # Check if feet are aligned
# #     if 10< angle_between_feet < 20:
# #         return True, "Feet aligned correctly"
# #     else:
# #         return False, f"Feet not aligned correctly. The angle between your feet is {angle_between_feet} degrees. Try to align your feet by bringing them closer together."
#
# # Fnction to check alignment of feet step 1u
#
#
# def check_alignment_of_feet(left_ankle, right_ankle, image, foot_position="parallel"):
#   """
#   Checks foot alignment in Tadasana pose using MediaPipe landmarks and optionally image processing.
#
#   Args:
#       left_ankle: A list containing x and y coordinates of the left ankle landmark.
#       right_ankle: A list containing x and y coordinates of the right ankle landmark.
#       image: (Optional) The input image (used for foot segmentation in big toe touching case).
#       foot_position: The chosen foot position ("big_toe_touch" or "parallel").
#
#   Returns:
#       A tuple containing a boolean (True if feet are aligned, False otherwise)
#       and a message indicating the result.
#   """
#
#   # Calculate absolute distance between ankles
#   ankle_distance = abs(left_ankle[0] - right_ankle[0])
#   image_width = image.shape[1] if image is not None else 1.0  # Use image width for normalization (or assume a default value)
#
#   # Define thresholds based on foot position (adjust as needed)
#   if foot_position == "big_toe_touch":
#     min_separation = 0.05 * image_width  # Narrower range for big toe touch
#     max_separation = 0.15 * image_width
#   else:
#     min_separation = 0.1 * image_width  # Wider range for parallel feet
#     max_separation = 0.3 * image_width
#
#   # Check if ankle distance falls within the desired range
#   if min_separation <= ankle_distance <= max_separation:
#     return True, "Feet aligned correctly"
#   else:
#     feedback_message = "Feet are not aligned correctly. "
#     if ankle_distance < min_separation:
#       feedback_message += f"Try bringing your big toes slightly closer together.{left_ankle}, {right_ankle}."
#     else:
#       feedback_message += f"Your feet might be too far apart. Try bringing them slightly closer together.{left_ankle}, {right_ankle}."
#     return False, feedback_message
#
#
#
#
#
#
# # Function to check engagement of thigh muscles step  2
# def check_engagement_of_thigh_muscles(left_hip, right_hip, left_knee, right_knee):
#     angle_left_thigh = calculate_angle(left_hip, left_knee, (left_knee[0], left_knee[1] + 1))
#     angle_right_thigh = calculate_angle(right_hip, right_knee, (right_knee[0], right_knee[1] + 1))
#     # Check if thigh muscles are engaged
#     if 175 < angle_left_thigh < 185 and 175 < angle_right_thigh < 185:
#         return True, "Thigh muscles engaged correctly"
#     else:
#         return False, f"Thigh muscles not engaged correctly. The angle of your left thigh is {angle_left_thigh} degrees and the angle of your right thigh is {angle_right_thigh} degrees. Engage your thigh muscles by straightening your legs."
#
# # Function to check pelvic alignment step 3
# def check_pelvic_alignment(left_hip, right_hip, left_shoulder, right_shoulder):
#     angle_left_pelvis = calculate_angle(left_hip, left_shoulder, (left_shoulder[0], left_shoulder[1] - 1))
#     angle_right_pelvis = calculate_angle(right_hip, right_shoulder, (right_shoulder[0], right_shoulder[1] - 1))
#     # Check if pelvis is aligned
#     if 170 < angle_left_pelvis < 190 and 170 < angle_right_pelvis < 190:
#         return True, "Pelvis aligned correctly"
#     else:
#         return False, f"Pelvis not aligned correctly. The angle of your left pelvis is {angle_left_pelvis} degrees and the angle of your right pelvis is {angle_right_pelvis} degrees. Align your pelvis by tucking your tailbone slightly under."
#
# # Function to check shoulder alignment step 4
# def check_shoulder_alignment(left_shoulder, right_shoulder, left_elbow, right_elbow):
#     angle_left_shoulder = calculate_angle(left_shoulder, left_elbow, (left_elbow[0], left_elbow[1] - 1))
#     angle_right_shoulder = calculate_angle(right_shoulder, right_elbow, (right_elbow[0], right_elbow[1] - 1))
#     # Check if shoulders are aligned
#     if 80 < angle_left_shoulder < 100 and 80 < angle_right_shoulder < 100:
#         return True, "Shoulders aligned correctly"
#     else:
#         return False, f"Shoulders not aligned correctly. The angle of your left shoulder is {angle_left_shoulder} degrees and the angle of your right shoulder is {angle_right_shoulder} degrees. Roll your shoulders back and down to open your chest."
#
# # Function to check arm position step 5
# def check_arm_position(left_shoulder, right_shoulder, left_elbow, right_elbow):
#     angle_left_arm = calculate_angle(left_shoulder, left_elbow, (left_shoulder[0], left_shoulder[1] + 1))
#     angle_right_arm = calculate_angle(right_shoulder, right_elbow, (right_shoulder[0], right_shoulder[1] + 1))
#     # Check if arms are in correct position
#     if 80 < angle_left_arm < 100 and 80 < angle_right_arm < 100:
#         return True, "Arms in correct position"
#     else:
#         return False, f"Arms not in correct position. The angle of your left arm is {angle_left_arm} degrees and the angle of your right arm is {angle_right_arm} degrees. Extend your arms parallel to the sides of your body."
#
#
#
# ##########################
# # Function to estimate pose using the provided image file
# def estimPose_img(input_file, pose=pose_img, landmarks_c=(234, 63, 247), connection_c=(117, 249, 77),
#                   thickness=2, circle_r=3, display=True):
#     if isinstance(input_file, str):
#         input_img = cv2.imread(input_file)
#     else:
#         input_img = input_file
#
#     # Create a copy of the input image
#     output_img = input_img.copy()
#
#     # Convert the image from BGR into RGB format.
#     RGB_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
#
#     # Perform the Pose Detection.
#     results = pose.process(RGB_img)
#
#     # Retrieve the height and width of the input image.
#     height, width, _ = input_img.shape
#
#     # Initialize a list to store the detected landmarks.
#     landmarks = []
#
#     # Check if any landmarks are detected.
#     if results.pose_landmarks:
#
#         # Draw Pose landmarks on the output image.
#         mp_drawing.draw_landmarks(output_img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                   mp_drawing.DrawingSpec(landmarks_c, thickness, circle_r),
#                                   mp_drawing.DrawingSpec(connection_c, thickness, circle_r))
#
#         # Iterate over the detected landmarks.
#         for landmark in results.pose_landmarks.landmark:
#             landmarks.append((int(landmark.x * width), int(landmark.y * height),
#                               (landmark.z * width)))
#
#     # Check if we want to display.
#     if display:
#         print("pose landmarks detected")
#         # Display the original input image and the resulting image.
#         plt.figure(figsize=[15, 15])
#         plt.subplot(121)
#         plt.imshow(input_img[:, :, ::-1])
#         plt.title("Original image")
#         plt.axis('off')
#         plt.subplot(122)
#         plt.imshow(output_img[:, :, ::-1])
#         plt.title("Output image")
#         plt.axis('off')
#
#         # Plot the Pose landmarks in 3D.
#         mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
#         # print(landmarks)
#
#     # Just get output_img and landmarks
#     else:
#         # Return the output image and the found landmarks.
#
#         return output_img, landmarks
#
#
# # Example usage for each step of Tadasana pose
# def estimate_tadasana_pose_steps():
#     # Initialize Mediapipe Pose class
#     mp_pose = mp.solutions.pose
#     pose_img = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)
#
#     # Provide paths to five images for each step
#     img_files = [
#         # r'D:\project\Research_Development\images\p1.jpg',
#         # r'D:\project\Research_Development\images\p2.jpg',
#         # r'D:\project\Research_Development\images\p3.jpg',
#         # r'D:\project\Research_Development\images\p4.jpg',
#         # r'D:\project\Research_Development\images\p5.jpg',
#         r'D:\project\Research_Development\images\t2.jpg',
#         r'D:\project\Research_Development\images\t1.png',
#         r'D:\project\Research_Development\images\legs-1.jpg',
#         r'D:\project\Research_Development\images\hand and leg-2.jpg',
#         r'D:\project\Research_Development\images\legs and hand 2-3.jpg',
#         r'D:\project\Research_Development\images\legs and hand-4.jpg',
#         r'D:\project\Research_Development\images\standing-5.jpg'
#     ]
#
#     for i, img_file in enumerate(img_files, start=1):
#         # Get image and landmarks
#         input_img = cv2.imread(img_file)
#         output_img, landmarks = estimPose_img(input_img, display=False)  # Call the function to get output image and landmarks
#
#         # Check each pose step
#         left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
#         right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
#         left_knee = landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value]
#         right_knee = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value]
#         left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
#         right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
#         left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
#         right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
#         left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
#         right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
#
#         if i == 1:
#             # Optional: Display the image with landmarks for visual feedback
#             plt.imshow(output_img[:, :, ::-1])
#             plt.title("Step_1 Pose Analysis")
#             plt.axis('off')
#             plt.show()
#             result, message = check_alignment_of_feet(left_ankle, right_ankle,input_img)
#         elif i == 2:
#             plt.imshow(output_img[:, :, ::-1])
#             plt.title("Step_2 Pose Analysis")
#             plt.axis('off')
#             plt.show()
#             result, message = check_engagement_of_thigh_muscles(left_hip, right_hip, left_knee, right_knee)
#         elif i == 3:
#             plt.imshow(output_img[:, :, ::-1])
#             plt.title("Step_3 Pose Analysis")
#             plt.axis('off')
#             plt.show()
#             result, message = check_pelvic_alignment(left_hip, right_hip, left_shoulder, right_shoulder)
#         elif i == 4:
#             plt.imshow(output_img[:, :, ::-1])
#             plt.title("Step_4 Pose Analysis")
#             plt.axis('off')
#             plt.show()
#             result, message = check_shoulder_alignment(left_shoulder, right_shoulder, left_elbow, right_elbow)
#         elif i == 5:
#             plt.imshow(output_img[:, :, ::-1])
#             plt.title("Step_5 Pose Analysis")
#             plt.axis('off')
#             plt.show()
#             result, message = check_arm_position(left_shoulder, right_shoulder, left_elbow, right_elbow)
#
#         print(f"Step {i}: {message}")
#
#
# # Call the function
# estimate_tadasana_pose_steps()
