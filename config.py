import argparse

class Config:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Motion Detection")

        # Video Source Options
        parser.add_argument("--video", type=str, help="Path to the video file")
        parser.add_argument("--webcam", action="store_true", help="Use webcam")

        # Motion Detection Parameters
        parser.add_argument("--motion-threshold", type=int, default=500, help="Minimum contour area to detect motion")
        parser.add_argument("--motion-hold", type=int, default=5, help="Number of frames to hold between motion checks")

        return parser.parse_args()