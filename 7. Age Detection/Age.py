import cv2

# Load the pre-trained Caffe model for age estimation
age_net = cv2.dnn.readNetFromCaffe("deploy_age.prototxt", "age_net.caffemodel")

# Function to estimate age from a face image
def estimate_age(face_image):
    # Resize the input image to the required input size of the model
    blob = cv2.dnn.blobFromImage(face_image, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

    # Set the input blob for the age estimation model
    age_net.setInput(blob)

    # Forward pass through the age estimation model
    age_preds = age_net.forward()

    # Get the predicted age
    predicted_age = int(age_preds[0])

    return predicted_age

# Function to detect faces and estimate age from webcam feed
def detect_and_estimate_age():
    # Initialize the webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the captured frame
        cv2.imshow('Video', frame)

        # Wait for key press and exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Call function to estimate age from the detected face
        age = estimate_age(gray)

        # Print the estimated age
        print(f"Estimated Age: {age} years")

    # Release the video capture
    video_capture.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Call the function to detect faces and estimate age from webcam feed
detect_and_estimate_age()
