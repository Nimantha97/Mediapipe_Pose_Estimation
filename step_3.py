#step_3
from AllMethods import *
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def check_arms_ups_right_side(left_hip, right_hip, left_shoulder, right_shoulder, left_elbow, right_elbow):
    angle_right_hand_and_hip = calculate_angle(right_hip, right_shoulder, right_elbow)

    if 165 < angle_right_hand_and_hip < 180:
        return True, f"Well done! Your hands are raised correctly which is {angle_right_hand_and_hip} degrees. Keep up the good work."
    else:
        return False, f"Your right hand is not raised high enough. Try to lift both hands above your shoulders, forming a straight line with your hips. The current angle of your right hand is {angle_right_hand_and_hip} degrees, and it should be closer to 180 degrees."

def check_alignment_of_hip_and_ankle_right_side(left_hip, right_hip, left_knee, right_knee, right_ankle, left_ankle):
    angle_left_leg = calculate_angle(left_hip, left_knee, left_ankle)
    angle_right_leg = calculate_angle(right_hip, right_knee, right_ankle)

    # Check if thigh muscles are engaged
    if 165 < angle_right_leg < 185:
        return True, f"Excellent! Your hips and legs are perfectly aligned which is {angle_right_leg} degree in the correct range, and your thigh muscles are engaged correctly. Keep up the great form."
    elif 165 > angle_right_leg:
        return False, f"Your right leg is not fully engaged. The angle between your right hip, knee, and ankle is {angle_right_leg} degrees, but it should be between 165 and 185 degrees for proper alignment. Try to straighten your right leg and engage your thigh muscles."

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
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y
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
        return False, "Sorry, the landmarks were not detected correctly. Please try again."

    # Calculate y-coordinate difference
    y_diff = abs(right_heel.y - right_foot_index.y)
    # y_diff = f"{y_diff:.3f}"

    # Calculate foot angle (optional)
    foot_angle = None
    if threshold_angle is not None:
        foot_angle = calculate_angle5(right_ankle, right_heel, right_foot_index)

    # Check if feet are flat based on thresholds
    if (y_diff <= threshold_y_diff and (foot_angle is None or foot_angle <= threshold_angle)):
        return False, f"Your feet are flat on the ground. To improve your form, try standing on your toes or balls of your feet. Your current foot angle is {foot_angle} degrees, and the y-difference between your big toe and heel is {y_diff}."
    else:
        return True, f"Great job! You're standing on your big toes correctly. Keep maintaining this form. Your current foot angle is {foot_angle} degrees, and the y-difference between your big toe and heel is {y_diff:.4f} , Y-difference value represents the vertical distance between your big toe and heel. \n It helps assess how much your foot is flexed during the pose."