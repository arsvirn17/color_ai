import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height /2)

    pixel_center = hsv_frame[cx, cy]
    hue_value = pixel_center[0]
    e_value = pixel_center[1]
    u_value = pixel_center[2]

    color = "Undefined"
    if hue_value < 5:
        color = "Red"
    elif hue_value < 22:
        color = "Orange"
    elif hue_value < 33:
        color = "Yellow"
    elif hue_value < 78:
        color = "Green"
    elif hue_value < 131:
        color = "Blue"
    elif hue_value < 170:
        color = "Pink"
    else:
        color = "Red"
    
    if e_value < 40:
        color = "White"

    if u_value < 40:
        color = "Black"

    pixel_center_bgr = frame[cx, cy]
    cv2.putText(frame, color, (200, 50), 0, 2, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()