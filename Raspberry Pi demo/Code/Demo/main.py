import cv2
import numpy as np
from picamera2 import Picamera2, Preview
from threading import Thread
import time

from Control import Control
from Ultrasonic import Ultrasonic
from PID import Incremental_PID
from FuzzyPID import FuzzyPID  # Assuming this is a defined class
from FuzzyController import FuzzyController  # Assuming this is a defined class for Fuzzy Logic based control

# Helper functions for color tracking
def find_ball(frame, color_range):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color_range[0], color_range[1])
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(largest)
        if radius > 10:  # Minimum size filter
            return int(x), int(y), int(radius)
    return None, None, None

# Main control class
class RobotControl:
    def __init__(self):
        self.camera = Picamera2()
        self.control = Control()
        self.ultrasonic = Ultrasonic()
        self.pid = Incremental_PID(0.1, 0.01, 0.01)
        self.fuzzy_pid = FuzzyPID(0.1, 0.01, 0.01)
        self.fuzzy = FuzzyController()
        self.running = True
        self.control_method = 'pid'  # Default to PID
        self.setup_camera()

    def setup_camera(self):
        config = self.camera.create_preview_configuration(main={"size": (640, 480)})
        self.camera.configure(config)
        self.preview = Preview()
        self.camera.set_preview(self.preview)
        self.camera.start()

    def process_control(self, control_type, error):
        if control_type == 'pid':
            return self.pid.PID_compute(error)
        elif control_type == 'fuzzy_pid':
            return self.fuzzy_pid.compute(error)
        elif control_type == 'fuzzy':
            return self.fuzzy.compute(error)
        else:
            return 0

    def run(self):
        try:
            self.control.forWard()
            while self.running:
                distance = self.ultrasonic.get_distance()
                if distance <= 10:
                    frame = self.camera.capture_array()
                    # Define HSV ranges for colors
                    red_range = (np.array([0, 120, 70]), np.array([10, 255, 255]))
                    blue_range = (np.array([110, 50, 50]), np.array([130, 255, 255]))
                    green_range = (np.array([50, 100, 100]), np.array([70, 255, 255]))

                    # Check for red ball
                    rx, ry, rradius = find_ball(frame, red_range)
                    if rx and ry:
                        self.control.turnRight()
                        time.sleep(0.5)  # Simulate 45-degree turn
                        continue

                    # Check for blue ball
                    bx, by, bradius = find_ball(frame, blue_range)
                    if bx and by:
                        self.control.turnLeft()
                        time.sleep(0.5)  # Simulate 45-degree turn
                        continue

                    # Check for green ball
                    gx, gy, gradius = find_ball(frame, green_range)
                    if gx and gy:
                        self.control.stop()
                        break

        finally:
            self.camera.stop()
            print("Camera stopped and robot halted.")

    def stop(self):
        self.running = False

if __name__ == '__main__':
    robot = RobotControl()
    control_thread = Thread(target=robot.run)
    control_thread.start()

    # Allow the user to change control methods on the fly
    while True:
        method = input("Enter control method (pid, fuzzy_pid, fuzzy): ")
        if method in ['pid', 'fuzzy_pid', 'fuzzy']:
            robot.control_method = method
        elif method == 'exit':
            robot.stop()
            break
        else:
            print("Invalid control method.")
