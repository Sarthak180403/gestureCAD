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
            h,w,_=frame.shape

            
            index_mcp=hand.landmark[5]
            index_pip=hand.landmark[6]
            index_dip=hand.landmark[7]
            index_tip=hand.landmark[8]

            index_mcp_x = int(index_mcp.x * w)
            index_mcp_y = int(index_mcp.y * h)

            index_pip_x = int(index_pip.x * w)
            index_pip_y = int(index_pip.y * h)

            index_dip_x = int(index_dip.x * w)
            index_dip_y = int(index_dip.y * h)

            index_tip_x = int(index_tip.x * w)
            index_tip_y = int(index_tip.y * h)

            # code to print in image coordinates
            # print(f"MCP: x={index_mcp.x:.2f}, y={index_mcp.y:.2f}")
            # print(f"PIP: x={index_pip.x:.2f}, y={index_pip.y:.2f}")
            # print(f"DIP: x={index_dip.x:.2f}, y={index_dip.y:.2f}")
            # print(f"TIP: x={index_tip.x:.2f}, y={index_tip.y:.2f}")

            # code to print in pixel coordinates 

            # print(f"MCP in pixel : x={index_mcp_x:.2f}, y={index_mcp_y:.2f}")
            # print(f"PIP in pixel : x={index_pip_x:.2f}, y={index_pip_y:.2f}")
            # print(f"DIP in pixel : x={index_dip_x:.2f}, y={index_dip_y:.2f}")
            # print(f"TIP in pixel : x={index_tip_x:.2f}, y={index_tip_y:.2f}")

        if index_tip_y< index_pip_y:
            print(" Index finger tip is above PIP")
        else:
            print("Index finger tip is below PIP")



    cv2.imshow("GestureCAD", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()