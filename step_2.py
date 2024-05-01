from AllMethods import *
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def check_alignment_of_hip_and_ankle(left_hip, right_hip, left_knee, right_knee, right_ankle, left_ankle):
    angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)
    angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)

    # Check if thigh muscles are engaged
    if 175 < angle_left_leg < 185 and 175 < angle_right_leg < 185:
        return True, f"Both hips and legs are engaged correctly in oneline (left hip and ankle = {angle_left_leg} degrees, right hip and ankle = {angle_right_leg} degrees)"
    elif 175 < angle_left_leg < 185 and 175 > angle_right_leg:
        return False, f"The right leg not engaged correctly. The angle of your right hip and ankle is {angle_right_leg} degrees and it should be in oneline"
    elif 175 > angle_left_leg and 175 < angle_right_leg < 185:
        return False, f"The left leg not engaged correctly. The angle of your left hip and ankle is {angle_left_leg} degrees and it should be in oneline"
    else:
        return False, "Both hips and legs are not engaged correctly ,those should be in oneline"


def check_arms_ups(left_hip, right_hip, left_shoulder,right_shoulder, left_elbow, right_elbow):

  angle_left_hand_and_hip = calculate_angle(left_hip, left_shoulder, left_elbow)
  angle_right_hand_and_hip = calculate_angle(right_hip, right_shoulder, right_elbow)

  if 165 < angle_left_hand_and_hip < 180 and 165 < angle_right_hand_and_hip < 180:
      return True, f"Both hands ups correctly (left hand = {angle_left_hand_and_hip}, right hand = {angle_right_hand_and_hip})"
  else:
      return False, f"please up your Both hands (left hand = {angle_left_hand_and_hip}, right hand = {angle_right_hand_and_hip})"



def calculate_angle_fingers(start_landmark, end_landmark):

    x1, y1 = start_landmark.x, start_landmark.y
    x2, y2 = end_landmark.x, end_landmark.y
    angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
    return angle


def check_fingers_locked(hand_landmarks):

        # Define the threshold angle for locked fingers (adjust as needed)
        threshold_angle = 10  # degrees

        # Define the finger connections (based on MediaPipe's HAND_CONNECTIONS)
        finger_connections = [
            [0, 1], [1, 2], [2, 3], [3, 4],  # Thumb
            [0, 5], [5, 6], [6, 7], [7, 8],  # Index finger
            [0, 9], [9, 10], [10, 11], [11, 12],  # Middle finger
            [0, 13], [13, 14], [14, 15], [15, 16],  # Ring finger
            [0, 17], [17, 18], [18, 19], [19, 20]  # Pinky
        ]

        # Iterate over the finger connections
        for conn in finger_connections:
            start_idx, end_idx = conn
            start_landmark = hand_landmarks[start_idx]
            end_landmark = hand_landmarks[end_idx]

            # Calculate the angle between the adjacent landmarks
            angle = calculate_angle_fingers(start_landmark, end_landmark)

            # Check if the angle is within the threshold
            if angle > threshold_angle:
                return False, "Fingers are not locked"

        # If all angles are within the threshold, return True
        return True, "Fingers are locked"
