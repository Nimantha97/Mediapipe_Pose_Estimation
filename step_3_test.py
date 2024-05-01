# from AllMethods import *
# import mediapipe as mp
#
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose()
#
#
# # def check_standing_on_big_toes1(results):
# #     # Thresholds (adjust as needed)
# #     threshold_foot_angle = 30  # degrees (Method 1)
# #     threshold_ankle_foot_distance = 0.2  # image resolution dependent (Method 2)
# #     threshold_ankle_knee_foot_angle = 160  # degrees (Method 2)
# #
# #     try:
# #         # Get relevant landmarks for both methods
# #         right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
# #         right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
# #         right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
# #         right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
# #
# #         # Method 1: Ankle, Heel, and Big Toe Angle
# #         foot_angle = calculate_angle(right_ankle, right_heel, right_foot_index)
# #         if foot_angle < threshold_foot_angle:
# #             return True, "Possible big toe stand detected (Method 1)"
# #
# #         # Method 2: Ankle, Knee, and Big Toe (consider both angle and distance)
# #         ankle_foot_distance = abs(right_ankle.y - right_foot_index.y)
# #         ankle_knee_foot_angle = calculate_angle(right_ankle, right_knee, right_foot_index)
# #         if ankle_knee_foot_angle > threshold_ankle_knee_foot_angle and ankle_foot_distance > threshold_ankle_foot_distance:
# #             return True, "Possible big toe stand detected (Method 2)"
# #
# #         # If neither method suggests big toe stand
# #         return False, "Big toe stand unlikely."
# #
# #     except:
# #         return False, "Landmarks not detected"
# #
# #
# # def check_standing_on_big_toes2(results):
# #     try:
# #         right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
# #         right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
# #         right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
# #     except:
# #         return False, "Landmarks not detected"
# #
# #     # Threshold values (adjust as needed)
# #     heel_height_threshold = 0.05  # Relative to ankle and foot index
# #
# #     # Check if the heel is significantly higher than the ankle and foot index
# #     if right_heel.y < right_ankle.y - heel_height_threshold and right_heel.y < right_foot_index.y - heel_height_threshold:
# #         return True, "Standing on big toes"
# #     else:
# #         return False, "Not standing on big toes"
# #
# #
# # # def check_standing_on_big_toes3(results):
# # #     try:
# # #         right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
# # #         right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
# # #         right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
# # #     except:
# # #         return False, "Landmarks not detected"
# # #
# # #     # Threshold angle for big toe stance (adjust as needed)
# # #     threshold_angle = 10  # degrees
# # #
# # #     # Calculate the angle between the foot and the horizontal
# # #     foot_angle = calculate_angle(right_ankle, right_foot_index,(1, 0))  # (1, 0) represents the horizontal
# # #
# # #     # Check if the foot angle is within the threshold for big toe stance
# # #     if foot_angle < threshold_angle:
# # #         return True, "Standing on big toes"
# # #     else:
# # #         return False, "Not standing on big toes"
# #
# # def check_standing_on_big_toes3(results):
# #     try:
# #         right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
# #         right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
# #         right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
# #     except:
# #         return False, "Landmarks not detected"
# #
# #     # Check if any of the landmarks are None
# #     if right_ankle is None or right_heel is None or right_foot_index is None:
# #         return False, "Landmarks not detected"
# #
# #     # Convert landmarks to tuples
# #     right_ankle = (right_ankle.x, right_ankle.y)
# #     right_foot_index = (right_foot_index.x, right_foot_index.y)
# #
# #     # Threshold angle for big toe stance (adjust as needed)
# #     threshold_angle = 10  # degrees
# #
# #     # Calculate the angle between the foot and the horizontal
# #     foot_angle = calculate_angle(right_ankle, right_foot_index, (1, 0))  # (1, 0) represents the horizontal
# #
# #     # Check if the foot angle is within the threshold for big toe stance
# #     if foot_angle < threshold_angle:
# #         return True, "Standing on big toes"
# #     else:
# #         return False, "Not standing on big toes"
# #
# #
# # def check_standing_big_toe4(right_ankle, right_heel, right_foot_index):
# #     # ankle_x, ankle_y = right_ankle[0], right_ankle[1]  # Assuming right_ankle is a tuple (x, y)
# #     # knee_x, knee_y = right_knee[0], right_knee[1]
# #     # foot_x, foot_y = right_foot[0], right_foot[1]
# #     #
# #     # angle = math.degrees(math.atan2(foot_y - ankle_y, foot_x - ankle_x))
# #     threshold_angle = 100  # Adjust based on expected leg bend
# #     #
# #     # # Calculate vertical distance (adjust threshold as needed)
# #     # distance = abs(ankle_y - foot_y)
# #     # threshold_distance = 0.2  # Adjust based on image resolution and foot size
# #     angle = calculate_angle(right_ankle, right_heel, right_foot_index)
# #     if angle > threshold_angle:
# #         return True, f"Possible big toe stand detected! = {angle}"
# #     else:
# #         return False, f"Big toe stand unlikely. = {angle}"
# #
#
# def check_arms_ups_right_side(left_hip, right_hip, left_shoulder, right_shoulder, left_elbow, right_elbow):
#     angle_right_hand_and_hip = calculate_angle(right_hip, right_shoulder, right_elbow)
#
#     if 165 < angle_right_hand_and_hip < 180:
#         return True, f"hands ups correctly ( right hand = {angle_right_hand_and_hip})"
#     else:
#         return False, f"please up your Both hands ( right hand = {angle_right_hand_and_hip})"
#
#
# def check_alignment_of_hip_and_ankle_right_side(left_hip, right_hip, left_knee, right_knee, right_ankle, left_ankle):
#     angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)
#     angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)
#
#     # Check if thigh muscles are engaged
#     if 165 < angle_right_leg < 185:
#         return True, f"Both hips and legs are engaged correctly in oneline ( right hip and ankle = {angle_right_leg} degrees)"
#     elif 165 > angle_right_leg:
#         return False, f"The right leg not engaged correctly. The angle of your right hip and ankle is {angle_right_leg} degrees and it should be in oneline"
#
# def calculate_angle5(p1, p2, p3):
#   """
#   Calculates the angle between three points using arctangent formula.
#
#   Args:
#       p1: Coordinates of the first point (x1, y1).
#       p2: Coordinates of the second point (x2, y2).
#       p3: Coordinates of the third point (x3, y3).
#
#   Returns:
#       The angle between the three points in degrees.
#   """
#   x1, y1 = p1.x , p1.y
#   x2, y2 = p2.x , p2.y
#   x3, y3 = p3.x , p3.y
#   radians = math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)
#   angle = math.degrees(radians)
#   # Handle negative angles (optional, adjust based on your coordinate system)
#   if angle < 0:
#     angle += 360
#   return angle
#
# def is_standing_on_big_toes(results, threshold_y_diff=0.1, threshold_angle=30):
#     try:
#         right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
#         right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
#         right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
#     except:
#         return False, "Landmarks not detected"
#
#     # Calculate y-coordinate difference
#     y_diff = abs(right_heel.y - right_foot_index.y)
#
#     # Calculate foot angle (optional)
#     foot_angle = None
#     if threshold_angle is not None:
#         foot_angle = calculate_angle5(right_ankle, right_heel, right_foot_index)
#
#     # Check if feet are flat based on thresholds
#     if (y_diff <= threshold_y_diff and (foot_angle is None or foot_angle <= threshold_angle)):
#         return False, f"Feet flat on ground - (foot angle = {foot_angle}, y_diff = {y_diff})"
#     else:
#         return True, f"Standing on big toe -  (foot angle = {foot_angle}, y_diff = {y_diff})"
