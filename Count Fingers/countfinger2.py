import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize hand detector to detect up to 2 hands
detector = HandDetector(maxHands=2, detectionCon=0.8)

# Initialize video capture
video = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = video.read()

    # If there is an issue with reading the frame, break the loop
    if not ret:
        print("Error reading frame from the video source.")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Find hands in the frame
    hands, _ = detector.findHands(frame)

    # If hands are detected
    if hands:
        for hand in hands:
            # Get landmark list of each hand
            lmList = hand["lmList"]

            # Count the number of fingers on each hand
            fingerCount = detector.fingersUp(hand)

            # Display the finger count on the frame for each hand
            cv2.putText(frame, f"Fingers: {fingerCount}", (int(lmList[0][0]), int(lmList[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow("Finger Count", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
video.release()
cv2.destroyAllWindows()
