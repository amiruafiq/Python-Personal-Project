import cv2

# Load pre-trained cascade classifiers for face, eye, and smile detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('smile_cascade.xml')

# Function to detect faces and smiles
def detect(gray_image, original_image):
    # Detect faces in the grayscale image
    face = face_cascade.detectMultiScale(gray_image, 1.3, 5)
    
    # Initialize variables to store total faces and smiley count
    total_faces = len(face)
    smiley_count = 0

    # Iterate through each detected face
    for (x, y, w, h) in face:
        # Draw rectangle around the face
        cv2.rectangle(original_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Extract region of interest (ROI) for face in grayscale and color
        roi_gray = gray_image[y:y+h, x:x+w]
        roi_color = original_image[y:y+h, x:x+w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            # Draw rectangle around each eye
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # Detect smiles within the face region
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in smiles:
            # Draw rectangle around each smile
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            # Increment smiley count
            smiley_count += 1

    # Calculate smiley detection percentage
    smiley_percentage = (smiley_count / total_faces) * 100 if total_faces > 0 else 0
    # Display smiley detection percentage on the image
    cv2.putText(original_image, f'Smiley Detection: {smiley_percentage:.2f}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    return original_image

# Open video capture device
video_capture = cv2.VideoCapture(0)

# Continuous loop for video capture and processing
while True:
    # Read a frame from the video capture device
    _, frame = video_capture.read()
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces and smiles in the frame
    canvas = detect(gray, frame)
    # Display the frame with detected faces and smiles
    cv2.imshow('Video', canvas)
    # Check for key press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device
video_capture.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
