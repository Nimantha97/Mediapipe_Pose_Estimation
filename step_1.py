from AllMethods import *
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


def check_alignment_of_hip_and_ankle(left_hip, right_hip, left_knee, right_knee, right_ankle, left_ankle):
    angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)
    angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)

    # Check if thigh muscles are engaged
    if 175 < angle_left_leg < 185 and 175 < angle_right_leg < 185:
        return True, print(f"Both hips and legs are engaged correctly (left hip and ankle = {angle_left_leg} degrees, right hip and ankle = {angle_right_leg} degrees)")
    elif 175 < angle_left_leg < 185 and 175 > angle_right_leg:
        return False, f"The right leg not engaged correctly. The angle of your right hip and ankle is {angle_right_leg} degrees and it should be in oneline"
    elif 175 > angle_left_leg and 175 < angle_right_leg < 185:
        return False, print(f"The left leg not engaged correctly. The angle of your left hip and ankle is {angle_left_leg} degrees and it should be in oneline")
    else:
        return False, "Both hips and legs are not engaged correctly ,those should be in oneline"

def check_arms_down(left_hip, right_hip, left_shoulder,right_shoulder, left_elbow, right_elbow):

  angle_left_hand_and_hip = calculate_angle(left_hip, left_shoulder, left_elbow)
  angle_right_hand_and_hip = calculate_angle(right_hip, right_shoulder, right_elbow)

  if 0 < angle_left_hand_and_hip < 30 and 0 < angle_right_hand_and_hip < 30:
      return True, f"Both hands down correctly (left hand = {angle_left_hand_and_hip}, right hand = {angle_right_hand_and_hip})"
  else:
      return False, f"please down your Both hands (left hand = {angle_left_hand_and_hip}, right hand = {angle_right_hand_and_hip})"



