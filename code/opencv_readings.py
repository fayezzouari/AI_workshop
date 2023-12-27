import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # 3. show the frames
    cv2.imshow("frame", frame)
    # 4. press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
