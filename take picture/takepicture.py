import cv2
import datetime
import time

def take_picture():
    # Open a connection to the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Allow the camera to warm up for 2 seconds
    print("Opening camera. Please wait...")
    time.sleep(2)

    # Capture a single frame
    ret, frame = cap.read()

    # Get the current date and time to use in the filename
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")

    # Save the captured frame to a file with the current date and time in the filename
    if ret:
        filename = f"captured_image_{formatted_datetime}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Picture taken successfully. Saved as {filename}.")
    else:
        print("Error: Failed to capture image.")

    # Release the camera
    cap.release()

if __name__ == "__main__":
    take_picture()
