import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Drawing utilities
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Resolution: {width} x {height}")
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert OpenCV image (BGR) to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb)

    # If hands are detected
    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            # Draw all 21 landmarks
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            # Print landmark coordinates
            for i, landmark in enumerate(hand.landmark):
                print(
                    f"Landmark {i}: "
                    f"x={landmark.x:.2f}, "
                    f"y={landmark.y:.2f}, "
                    f"z={landmark.z:.2f}"
                )
                #code for thumb 
                # thumb_tip=hand.landmark[4]
                # ht,wt,_=frame.shape
                # cxt=int (thumb_tip.x*wt)
                # cyt=int(thumb_tip.y*ht)

                # cv2.putText((frame,str(i),(40,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2))
                # finger_tip=hand.landmark[i]
                # h, w, _ = frame.shape
                # cx = int(finger_tip.x * w)
                # cy = int(finger_tip.y * h)
                # cv2.putText(frame,
                #             str(i),
                #             (cx,cy),
                #             cv2.FONT_HERSHEY_COMPLEX,
                #             1,
                #             (255,255,255),
                #             2)
                thumb_tip = hand.landmark[4]
                index_tip = hand.landmark[8]
                middle_tip = hand.landmark[12]
                ring_tip = hand.landmark[16]
                pinky_tip = hand.landmark[20]
                h, w, _ = frame.shape
                cx = int(thumb_tip.x * w)
                cy = int(thumb_tip.y * h)
                cv2.putText(frame,
                            str(4),
                            (cx,cy),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255,255,255),
                            2)


            # print(f"Index Finger : ({cx}, {cy})")



            # cv2.circle(frame, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
            
    print("-" * 40)
    cv2.imshow("GestureCAD", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()