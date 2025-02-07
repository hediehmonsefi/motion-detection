import cv2
from config import Config
from motion_detection import MotionDetection


def main():
    # Parse command-line arguments
    args = Config.parse_args()

    # Select video source
    if args.webcam:
        cap = cv2.VideoCapture(0)  # Open webcam
    elif args.video:
        cap = cv2.VideoCapture(args.video)  # Open provided video file
    else:
        print("Error: You must provide --video <path> or use --webcam")
        return

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return


    # Initialize motion detection with default parameters
    motion_detector = MotionDetection(motion_hold=args.motion_hold, motion_threshold=args.motion_threshold)

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or error reading frame.")
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