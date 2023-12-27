from pushbullet import Pushbullet
import cv2
from ClassificationModule import Classifier
import urllib.request
import numpy as np

API_KEY = "o.2CObAO4b1i3l4YyYkA72xg9BWSdxImqI"


pb = Pushbullet(API_KEY)


url = "http://192.168.0.50/cam-hi.jpg"

mydata = Classifier(
    r"C:\Users\AsusExpertBook\Documents\HYPERIMPORTANT\ATAST\wintercamp2023\workshop\code\keras_model.h5",
    r"C:\Users\AsusExpertBook\Documents\HYPERIMPORTANT\ATAST\wintercamp2023\workshop\code\labels.txt",
)

count = 0

cap = cv2.VideoCapture(0)
while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    predict, index = mydata.getPrediction(img, color=(0, 0, 255))
    print(predict, index)

    if index == 0:
        count += 1

    if count == 30:
        push = pb.push_note("You Counter today: ", "Sabrine is detected")
        count = 0

    cv2.imshow("Video Frame", img)
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
