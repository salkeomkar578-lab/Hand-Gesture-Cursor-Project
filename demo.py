#!/usr/bin/env python3
"""
Demo script for Hand Gesture Cursor Control

This script demonstrates the hand gesture cursor functionality
with additional debug information and testing features.
"""

import cv2
import mediapipe as mp
import time

class HandGestureDemo:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
    def run_demo(self):
        """Run demo without cursor control for testing"""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open camera")
            return
            
        print("Demo mode - showing hand tracking without cursor control")
        print("Press 'q' to quit")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Show landmark positions
                    landmarks = hand_landmarks.landmark
                    index_tip = landmarks[8]
                    thumb_tip = landmarks[4]
                    
                    h, w, _ = frame.shape
                    cv2.circle(frame, (int(index_tip.x * w), int(index_tip.y * h)), 10, (0, 255, 0), -1)
                    cv2.circle(frame, (int(thumb_tip.x * w), int(thumb_tip.y * h)), 10, (255, 0, 0), -1)
                    
            cv2.putText(frame, "DEMO MODE - Hand tracking only", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "Green: Index finger, Blue: Thumb", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow('Hand Gesture Demo', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    demo = HandGestureDemo()
    demo.run_demo()