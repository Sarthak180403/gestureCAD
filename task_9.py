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

            for i,landmark in enumerate(hand.landmark):
                print(
                    f"Landmark {i}:"
                    f"x={landmark.x:.2f}, "
                    f"y={landmark.y:.2f}, "
                    f"z={landmark.z:.2f}"
                )
                h,w,_=frame.shape
                fingertips=[4,8,12,16,20]
                for tip_id in fingertips:
                    landmark=hand.landmark[tip_id]

                    cx=int(landmark.x*w)
                    cy=int(landmark.y*h)

                    cv2.circle(frame,
                               (cx,cy),
                               8,
                               (255,0,0),
                               10)
    cv2.imshow("GestureCAD", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()