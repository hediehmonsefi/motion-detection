import cv2
import numpy as np


class MotionDetection:
    """
    A class for detecting motion in video frames.
    """

    def __init__(self, motion_hold=5, motion_threshold=500):
        """
        Initialize the motion detection parameters.

        Args:
            motion_hold (int): Number of frames to hold between motion checks.
            motion_threshold (int): Minimum contour area to detect motion.
        """
        self.motion_hold = motion_hold
        self.motion_threshold = motion_threshold
        self.hold_count = 0
        self.first_frame = None
        self.second_frame = None
        self.motion_flag = True

    @staticmethod
    def prepare_gray(frame):
        """
        Convert a frame to grayscale and apply Gaussian blur.

        Args:
            frame (ndarray): Input RGB frame.

        Returns:
            ndarray: Processed grayscale frame.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        return gray

    def motion_detection(self, first_frame, second_frame, frame):
        """
        Detect motion by comparing two consecutive frames.

        Args:
            first_frame (ndarray): First grayscale frame.
            second_frame (ndarray): Second grayscale frame.
            frame (ndarray): Original frame.

        Returns:
            tuple: (bool, ndarray) Motion detected flag and annotated frame.
        """
        result = False

        # Calculate frame difference and threshold it
        frame_delta = cv2.absdiff(first_frame, second_frame)
        kernel = np.ones((5, 5), np.uint8)
        frame_delta = cv2.dilate(frame_delta, kernel, iterations=1)
        thresh = cv2.threshold(frame_delta, 20, 255, cv2.THRESH_BINARY)[1]

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > self.motion_threshold:
                result = True
                # break
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        return result, frame

    def process_frame(self, frame):
        """
        Process a frame and check for motion.

        Args:
            frame (ndarray): Input frame.

        Returns:
            tuple: (bool, ndarray) Motion detected flag and processed frame.
        """
        if self.hold_count % self.motion_hold == 0:
            gray_frame = self.prepare_gray(frame)
            self.second_frame = gray_frame

            if self.first_frame is not None and self.second_frame is not None:
                self.motion_flag, frame = self.motion_detection(self.first_frame, self.second_frame, frame)

            self.hold_count = 0

        self.hold_count += 1
        self.first_frame = self.second_frame

        return self.motion_flag, frame