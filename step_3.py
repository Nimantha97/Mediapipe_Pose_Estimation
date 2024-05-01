from AllMethods import *
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


def check_arms_ups_right_side(left_hip, right_hip, left_shoulder, right_shoulder, left_elbow, right_elbow):
    angle_right_hand_and_hip = calculate_angle(right_hip, right_shoulder, right_elbow)

    if 165 < angle_right_hand_and_hip < 180:
        return True, f"hands ups correctly ( right hand = {angle_right_hand_and_hip})"
    else:
        return False, f"please up your Both hands ( right hand = {angle_right_hand_and_hip})"


def check_alignment_of_hip_and_ankle_right_side(left_hip, right_hip, left_knee, right_knee, right_ankle, left_ankle):
    angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)
    angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)

    # Check if thigh muscles are engaged
    if 165 < angle_right_leg < 185:
        return True, f"Both hips and legs are engaged correctly in oneline ( right hip and ankle = {angle_right_leg} degrees)"
    elif 165 > angle_right_leg:
        return False, f"The right leg not engaged correctly. The angle of your right hip and ankle is {angle_right_leg} degrees and it should be in oneline"

def calculate_angle5(p1, p2, p3):
  """
  Calculates the angle between three points using arctangent formula.

  Args:
      p1: Coordinates of the first point (x1, y1).
      p2: Coordinates of the second point (x2, y2).
      p3: Coordinates of the third point (x3, y3).

  Returns:
      The angle between the three points in degrees.
  """
  x1, y1 = p1.x , p1.y
  x2, y2 = p2.x , p2.y
  x3, y3 = p3.x , p3.y
  radians = math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)
  angle = math.degrees(radians)

  # Handle negative angles (optional, adjust based on your coordinate system)
  if angle < 0:
    angle += 360
  return int(angle)

def is_standing_on_big_toes(results, threshold_y_diff=0.1, threshold_angle=30):
    try:
        right_ankle = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
        right_heel = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
        right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
    except:
        return False, "Landmarks not detected"

    # Calculate y-coordinate difference
    y_diff = abs(right_heel.y - right_foot_index.y)
    # y_diff = f"{y_diff:.3f}"

    # Calculate foot angle (optional)
    foot_angle = None
    if threshold_angle is not None:
        foot_angle = calculate_angle5(right_ankle, right_heel, right_foot_index)

    # Check if feet are flat based on thresholds
    if (y_diff <= threshold_y_diff and (foot_angle is None or foot_angle <= threshold_angle)):
        return False, f"Feet flat on ground : (foot angle = {foot_angle}, y_diff = {y_diff})"
    else:
        return True, f"Standing on big toe correctly :  (foot angle = {foot_angle}, y_diff = {y_diff} [Y-difference (y_diff): This value represents the vertical distance between your big toe and heel. \n It helps assess how much your foot is flexed during the pose. ]  )"
