#step_1
from AllMethods import *
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def check_alignment_of_hip_and_ankle(left_hip, right_hip, left_knee, right_knee, right_ankle, left_ankle):
    angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)
    angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)

    # Check if thigh muscles are engaged
    if 175 < angle_left_leg < 185 and 175 < angle_right_leg < 185:
        return True, f"Well done! Both your hips and legs are engaged correctly. The ideal angle range for proper alignment is between 175 and 185 degrees. Your left hip and ankle angle is {angle_left_leg} degrees, and your right hip and ankle angle is {angle_right_leg} degrees."
    elif 175 < angle_left_leg < 185 and 175 > angle_right_leg:
        return False, f"Your right leg is not engaged correctly. The angle of your right hip and ankle is {angle_right_leg} degrees, but it should be between 175 and 185 degrees for proper alignment. Try to straighten your right leg and engage your thigh muscles."
    elif 175 > angle_left_leg and 175 < angle_right_leg < 185:
        return False, f"Your left leg is not engaged correctly. The angle of your left hip and ankle is {angle_left_leg} degrees, but it should be between 175 and 185 degrees for proper alignment. Try to straighten your left leg and engage your thigh muscles."
    else:
        return False, "Both your hips and legs are not engaged correctly. The ideal angle range for proper alignment is between 175 and 185 degrees. Please try to straighten your legs and engage your thigh muscles."

def check_arms_down(left_hip, right_hip, left_shoulder, right_shoulder, left_elbow, right_elbow):
    angle_left_hand_and_hip = calculate_angle(left_hip, left_shoulder, left_elbow)
    angle_right_hand_and_hip = calculate_angle(right_hip, right_shoulder, right_elbow)

    if 0 < angle_left_hand_and_hip < 30 and 0 < angle_right_hand_and_hip < 30:
        return True, f"Great job! Both your hands are down correctly. The ideal angle range for the arms is between 0 and 30 degrees. Your left hand angle is {angle_left_hand_and_hip} degrees, and your right hand angle is {angle_right_hand_and_hip} degrees."
    else:
        return False, f"Your arms are not in the correct position. The ideal angle range for the arms is between 0 and 30 degrees. Your left hand angle is {angle_left_hand_and_hip} degrees, and your right hand angle is {angle_right_hand_and_hip} degrees. Please lower your arms and try to keep them within the recommended range."