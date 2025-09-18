#!/usr/bin/env python3
"""
Hand Gesture Cursor Control

This script uses computer vision to control the computer cursor with hand gestures.
It uses MediaPipe for hand tracking and PyAutoGUI for cursor control.

Author: Hand-Gesture-Cursor-Project
License: MIT
"""

import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import math
from config import *

class HandGestureCursor:
    def __init__(self):
        # Initialize MediaPipe hands solution
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
        # Screen dimensions
        self.screen_width, self.screen_height = pyautogui.size()
        
        # Camera dimensions
        self.cam_width = CAMERA_WIDTH
        self.cam_height = CAMERA_HEIGHT
        
        # Smoothing parameters
        self.smoothening = SMOOTHENING_FACTOR
        self.prev_x, self.prev_y = 0, 0
        
        # Click detection parameters
        self.clicking = False
        self.click_threshold = CLICK_THRESHOLD
        self.last_click_time = 0
        self.click_cooldown = CLICK_COOLDOWN
        
        # Configure PyAutoGUI
        pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort
        pyautogui.PAUSE = 0.01  # Small pause between actions
        
        print("Hand Gesture Cursor Control Initialized")
        print("Move your index finger to control the cursor")
        print("Pinch thumb and index finger together to left click")
        print("Move mouse to top-left corner to exit")

    def get_distance(self, p1, p2):
        """Calculate Euclidean distance between two points"""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def is_click_gesture(self, landmarks):
        """Detect if thumb and index finger are close enough for a click"""
        # Get thumb tip and index finger tip positions
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        
        # Calculate distance between thumb and index finger
        distance = self.get_distance(
            [thumb_tip.x * self.cam_width, thumb_tip.y * self.cam_height],
            [index_tip.x * self.cam_width, index_tip.y * self.cam_height]
        )
        
        return distance < self.click_threshold

    def smooth_cursor_movement(self, x, y):
        """Apply smoothing to cursor movement"""
        # Smoothen the cursor movement
        self.prev_x = self.prev_x + (x - self.prev_x) / self.smoothening
        self.prev_y = self.prev_y + (y - self.prev_y) / self.smoothening
        
        return int(self.prev_x), int(self.prev_y)

    def run(self):
        """Main execution loop"""
        # Initialize camera
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cam_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cam_height)
        
        if not cap.isOpened():
            print("Error: Could not open camera")
            return
        
        print("Camera initialized. Press 'q' to quit or move mouse to top-left corner.")
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not read frame")
                    break
                
                # Flip frame horizontally for mirror effect
                frame = cv2.flip(frame, 1)
                
                # Convert BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Process the frame
                results = self.hands.process(rgb_frame)
                
                # Draw hand landmarks if detected
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        # Draw landmarks
                        self.mp_drawing.draw_landmarks(
                            frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                        )
                        
                        # Get landmark positions
                        landmarks = hand_landmarks.landmark
                        
                        # Get index finger tip position (landmark 8)
                        index_tip = landmarks[8]
                        
                        # Convert to screen coordinates
                        x = int(index_tip.x * self.screen_width)
                        y = int(index_tip.y * self.screen_height)
                        
                        # Apply smoothing
                        smooth_x, smooth_y = self.smooth_cursor_movement(x, y)
                        
                        # Move cursor
                        pyautogui.moveTo(smooth_x, smooth_y)
                        
                        # Check for click gesture
                        current_time = time.time()
                        if self.is_click_gesture(landmarks):
                            if not self.clicking and (current_time - self.last_click_time) > self.click_cooldown:
                                pyautogui.click()
                                self.clicking = True
                                self.last_click_time = current_time
                                print("Click detected!")
                        else:
                            self.clicking = False
                        
                        # Draw cursor position indicator on frame
                        cv2.circle(frame, 
                                 (int(index_tip.x * self.cam_width), 
                                  int(index_tip.y * self.cam_height)), 
                                 10, (0, 255, 0), -1)
                
                # Add instructions to frame
                cv2.putText(frame, "Move index finger to control cursor", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(frame, "Pinch thumb+index to click", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(frame, "Press 'q' to quit", 
                           (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                # Display frame
                cv2.imshow('Hand Gesture Cursor Control', frame)
                
                # Check for quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Cleanup
            cap.release()
            cv2.destroyAllWindows()
            print("Camera released and windows closed")

def main():
    """Main function"""
    print("Starting Hand Gesture Cursor Control...")
    print("Make sure your camera is connected and working")
    
    try:
        gesture_cursor = HandGestureCursor()
        gesture_cursor.run()
    except Exception as e:
        print(f"Failed to start application: {e}")
        print("Please check that your camera is working and try again")

if __name__ == "__main__":
    main()