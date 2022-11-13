import cv2
import mediapipe as mp
import numpy as np
import math

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)
chords = "Major"
chords_val = 0
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        frame = cv2.resize(frame, (0, 0), fx = 1.6, fy = 1.6)
        h, w, c = frame.shape
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        try:
            landmarks = results.pose_landmarks.landmark

            nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x * w,landmarks[mp_pose.PoseLandmark.NOSE.value].y * h]
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x * w,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y * h]
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x * w,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y * h]
            right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x * w,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y * h]
            right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x * w,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y * h]
            left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x * w,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y * h]
            sd = shoulder_dist = math.sqrt(((left_shoulder[0] - right_shoulder[0]) ** 2) + ((left_shoulder[1] - right_shoulder[1]) ** 2))
            print(left_shoulder[0], left_shoulder[1], right_shoulder[0], right_shoulder[1], shoulder_dist)

            image = cv2.line(image, (int(left_shoulder[0]), int(right_elbow[1])), (int(right_shoulder[0]), int(right_elbow[1])), color, 5)
            
            fret1 = int(left_shoulder[0] + sd/4)
            fret2 = int(left_shoulder[0] + sd/7 + sd/4)
            fret3 = int(left_shoulder[0] + sd/7 + sd/7 + sd/4)
            fret4 = int(left_shoulder[0] + sd/7 + sd/7 + sd/7 + sd/4)
            fret5 = int(left_shoulder[0] + sd/7 + sd/7 + sd/7 + sd/7 + sd/4)
            fret6 = int(left_shoulder[0] + sd/7 + sd/7 + sd/7 + sd/7 + sd/7 + sd/4)
            fret7 = int(left_shoulder[0] + sd/7 + sd/7 + sd/7 + sd/7 + sd/7 + sd/7 + sd/4)
            
            image = cv2.line(image, (fret1, int(left_shoulder[1] - 50)), (fret1, int(left_shoulder[1] + 200)), color, 2)
            image = cv2.line(image, (fret2, int(left_shoulder[1] - 50)), (fret2, int(left_shoulder[1] + 200)), color, 2)
            image = cv2.line(image, (fret3, int(left_shoulder[1] - 50)), (fret3, int(left_shoulder[1] + 200)), color, 2)
            image = cv2.line(image, (fret4, int(left_shoulder[1] - 50)), (fret4, int(left_shoulder[1] + 200)), color, 2)
            image = cv2.line(image, (fret5, int(left_shoulder[1] - 50)), (fret5, int(left_shoulder[1] + 200)), color, 2)
            image = cv2.line(image, (fret6, int(left_shoulder[1] - 50)), (fret6, int(left_shoulder[1] + 200)), color, 2)
            image = cv2.line(image, (fret7, int(left_shoulder[1] - 50)), (fret7, int(left_shoulder[1] + 200)), color, 2)
            
            image = cv2.circle(image, (int(right_wrist[0]), int(right_wrist[1])), 10 , color, -1)
            image = cv2.circle(image, (int(left_wrist[0]), int(left_wrist[1])), 10 , color, -1)
            
            if(right_wrist[1] >= right_elbow[1]):
                if(sound_val == 0):
                    sound_val = 1
                    
                    if(left_wrist[0] <= fret1):
                        image = cv2.putText(image, 'Tune1', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] <= fret2 and left_wrist[0] > fret1):
                        image = cv2.putText(image, 'Tune2', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] <= fret3 and left_wrist[0] > fret2):
                        image = cv2.putText(image, 'Tune3', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] <= fret4 and left_wrist[0] > fret3):
                        image = cv2.putText(image, 'Tune4', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] <= fret5 and left_wrist[0] > fret4):
                        image = cv2.putText(image, 'Tune5', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] <= fret6 and left_wrist[0] > fret5):
                        image = cv2.putText(image, 'Tune6', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] <= fret7 and left_wrist[0] > fret6):
                        image = cv2.putText(image, 'Tune7', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    if(left_wrist[0] > fret7):
                        image = cv2.putText(image, 'Tune8', (50,50), font, 1, color, 2, cv2.LINE_AA)
                    
            if(right_wrist[1] < right_elbow[1]):
                sound_val = 0
                
#             chords = "Major"    
            if(left_wrist[1] <= nose[1]):
                if(chords_val == 1):
                    chords_val = 0
            if(left_wrist[1] > nose[1]):
                chords_val = 1
                
            if(chords_val == 0):
                if(chords == "Minor"):
                    chords = "Major"
                    chords_val = 2
                elif(chords == "Major"):
                    chords = "Minor"
                    chords_val = 2
            
            image = cv2.putText(image, chords, (50,200), font, 1, color, 2, cv2.LINE_AA)
        
        except:
            pass
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
