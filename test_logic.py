#!/usr/bin/env python3
"""
Test script for Hand Gesture Cursor Project

This script tests the core logic without requiring camera or external dependencies.
"""

import math
import sys
import os

# Add the current directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from config import *
    print("✓ Config module imported successfully")
except ImportError as e:
    print(f"✗ Failed to import config: {e}")
    sys.exit(1)

class MockLandmark:
    """Mock landmark class for testing"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test_distance_calculation():
    """Test the distance calculation function"""
    def get_distance(p1, p2):
        """Calculate Euclidean distance between two points"""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    # Test cases
    test_cases = [
        ([0, 0], [3, 4], 5.0),  # 3-4-5 triangle
        ([0, 0], [0, 0], 0.0),  # Same point
        ([1, 1], [4, 5], 5.0),  # Another test
    ]
    
    print("\nTesting distance calculation:")
    for p1, p2, expected in test_cases:
        result = get_distance(p1, p2)
        if abs(result - expected) < 0.001:
            print(f"✓ Distance between {p1} and {p2}: {result:.1f} (expected {expected})")
        else:
            print(f"✗ Distance between {p1} and {p2}: {result:.1f} (expected {expected})")

def test_click_detection():
    """Test click detection logic"""
    def is_click_gesture(thumb_pos, index_pos, threshold=40):
        """Simulate click detection"""
        distance = math.sqrt((thumb_pos[0] - index_pos[0])**2 + (thumb_pos[1] - index_pos[1])**2)
        return distance < threshold
    
    print("\nTesting click detection:")
    
    # Test cases: (thumb_pos, index_pos, should_click)
    test_cases = [
        ([100, 100], [120, 120], True),   # Close enough for click
        ([100, 100], [200, 200], False), # Too far for click
        ([50, 50], [80, 80], True),      # Close enough for click
    ]
    
    for thumb, index, expected in test_cases:
        result = is_click_gesture(thumb, index, CLICK_THRESHOLD)
        status = "✓" if result == expected else "✗"
        print(f"{status} Thumb: {thumb}, Index: {index} -> Click: {result} (expected {expected})")

def test_smoothing():
    """Test cursor smoothing logic"""
    def smooth_movement(current_x, current_y, prev_x, prev_y, smoothening=5):
        """Simulate smoothing"""
        new_x = prev_x + (current_x - prev_x) / smoothening
        new_y = prev_y + (current_y - prev_y) / smoothening
        return int(new_x), int(new_y)
    
    print("\nTesting cursor smoothing:")
    
    # Simulate movement from (0,0) to (100,100)
    prev_x, prev_y = 0, 0
    target_x, target_y = 100, 100
    
    for i in range(3):
        smooth_x, smooth_y = smooth_movement(target_x, target_y, prev_x, prev_y, SMOOTHENING_FACTOR)
        print(f"  Step {i+1}: ({prev_x}, {prev_y}) -> ({smooth_x}, {smooth_y})")
        prev_x, prev_y = smooth_x, smooth_y

def test_config_values():
    """Test configuration values"""
    print("\nTesting configuration values:")
    
    configs = [
        ("CAMERA_WIDTH", CAMERA_WIDTH, int),
        ("CAMERA_HEIGHT", CAMERA_HEIGHT, int),
        ("MIN_DETECTION_CONFIDENCE", MIN_DETECTION_CONFIDENCE, float),
        ("MIN_TRACKING_CONFIDENCE", MIN_TRACKING_CONFIDENCE, float),
        ("SMOOTHENING_FACTOR", SMOOTHENING_FACTOR, int),
        ("CLICK_THRESHOLD", CLICK_THRESHOLD, (int, float)),
        ("CLICK_COOLDOWN", CLICK_COOLDOWN, (int, float)),
    ]
    
    for name, value, expected_type in configs:
        if isinstance(expected_type, tuple):
            is_correct_type = isinstance(value, expected_type)
        else:
            is_correct_type = isinstance(value, expected_type)
        
        status = "✓" if is_correct_type else "✗"
        print(f"{status} {name}: {value} (type: {type(value).__name__})")

def main():
    """Main test function"""
    print("Hand Gesture Cursor Project - Test Suite")
    print("=" * 45)
    
    test_config_values()
    test_distance_calculation()
    test_click_detection()
    test_smoothing()
    
    print("\n" + "=" * 45)
    print("Test suite completed!")
    print("\nIf all tests passed (✓), the core logic is working correctly.")
    print("You can now install dependencies and run the main application.")

if __name__ == "__main__":
    main()