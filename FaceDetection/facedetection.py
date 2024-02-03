import cv2
import torch
from torchvision import transforms
from fer import FER

def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    return faces, gray

def detect_emotion(face, emotion_model):
    roi = cv2.resize(face, (48, 48))
    tensor_img = transforms.ToTensor()(roi).unsqueeze(0)
    emotion = emotion_model.predict(tensor_img)[0]

    return emotion

def main():
    # Load the pre-trained face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the pre-trained emotion detection model
    emotion_model = FER()

    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture a single frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Perform face detection
        faces, gray = detect_faces(frame, face_cascade)

        for (x, y, w, h) in faces:
            # Extract the detected face
            detected_face = gray[y:y+h, x:x+w]

            # Perform emotion detection
            emotion = detect_emotion(detected_face, emotion_model)

            # Display the emotion text
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow("Emotion Detection", frame)

        # Break the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
