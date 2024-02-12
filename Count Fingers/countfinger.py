#code from https://github.com/vamshi6763/fingers_count_using_openCV/blob/main/main.py
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                print("0")
            if fingerup == [0, 1, 0, 0, 0]:
                print("1")
            if fingerup == [0, 1, 1, 0, 0]:
                print("2")
            if fingerup == [0, 1, 1, 1, 0]:
                print("3")
            if fingerup == [0, 1, 1, 1, 1]:
                print("4")
            if fingerup == [1, 1, 1, 1, 1]:
                print("5")
            if fingerup == [1, 0, 0, 0, 0]:
                print("6")
            if fingerup == [1, 1, 0, 0, 0]:
                print("7")
            if fingerup == [1, 1, 1, 0, 0]:
                print("8")
            if fingerup == [1, 1, 1, 1, 0]:
                print("9")

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
