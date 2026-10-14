import cv2

# Open the default webcam (0 = first camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    # Read one frame from the webcam
    ret, frame = cap.read()

    # If no frame is received, stop the program
    if not ret:
        print("Error: Could not read frame.")
        break
    #print(frame.shape) jUST TO READ THE FRAME SHAPE 
    cv2.circle(frame,(100,100),20,(0,255,0),-1) # to draw the circle 
    cv2.rectangle(frame,(0,0),(250,150),(0,0,255),2) # to draw the rectangle 
    cv2.line(frame,(240,320),(240,360),(255,0,0),2) # to draw the line\
    cv2.line(frame,(200,340),(280,340),(255,0,0),2) 
    cv2.putText(frame,"Gesture CAD ",(40,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    # Display the frame
    cv2.imshow("GestureCAD - Webcam", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Closing.......")
        break
print("Releasing CAMERA...")


# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
print("Program ended.............")
print(frame.shape)