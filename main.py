import cv2
from motion_detection import MotionDetection


def main():
    # Initialize motion detection with default parameters
    motion_detector = MotionDetection(motion_threshold=100)

    # Open webcam
    cap = cv2.VideoCapture("/Users/hedieh/Documents/AI/git/motionDetection/motion.mp4")

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame for motion detection
        motion_detected, processed_frame = motion_detector.process_frame(frame)

        # Annotate the frame
        text = "Motion Detected" if motion_detected else "No Motion"
        color = (0, 255, 0) if motion_detected else (0, 0, 255)
        cv2.putText(processed_frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # Show the frame
        cv2.imshow("Motion Detection", processed_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()