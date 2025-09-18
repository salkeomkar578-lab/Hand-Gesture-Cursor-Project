#!/usr/bin/env python3
"""
Setup script for Hand Gesture Cursor Project

This script checks dependencies and provides installation guidance.
"""

import sys
import subprocess
import importlib

def check_python_version():
    """Check if Python version is compatible"""
    required_version = (3, 7)
    current_version = sys.version_info[:2]
    
    if current_version >= required_version:
        print(f"✓ Python {sys.version.split()[0]} is compatible")
        return True
    else:
        print(f"✗ Python {'.'.join(map(str, required_version))} or higher is required")
        print(f"  Current version: {'.'.join(map(str, current_version))}")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✓ {package_name} is installed")
        return True
    except ImportError:
        print(f"✗ {package_name} is not installed")
        return False

def install_packages():
    """Attempt to install required packages"""
    packages = [
        "opencv-python",
        "mediapipe", 
        "pyautogui",
        "numpy"
    ]
    
    print("\nAttempting to install packages...")
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install {package}")
            return False
    
    return True

def main():
    """Main setup function"""
    print("Hand Gesture Cursor Project Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        print("\nPlease update Python and try again.")
        return False
    
    print("\nChecking dependencies...")
    
    # Check required packages
    required_packages = [
        ("opencv-python", "cv2"),
        ("mediapipe", "mediapipe"),
        ("pyautogui", "pyautogui"),
        ("numpy", "numpy")
    ]
    
    missing_packages = []
    for package_name, import_name in required_packages:
        if not check_package(package_name, import_name):
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        
        user_input = input("\nWould you like to install missing packages? (y/n): ")
        if user_input.lower() in ['y', 'yes']:
            if install_packages():
                print("\n✓ All packages installed successfully!")
                print("\nYou can now run the hand gesture cursor with:")
                print("python hand_gesture_cursor.py")
            else:
                print("\n✗ Some packages failed to install.")
                print("Please install them manually using:")
                print("pip install opencv-python mediapipe pyautogui numpy")
        else:
            print("\nPlease install the missing packages manually:")
            print("pip install opencv-python mediapipe pyautogui numpy")
    else:
        print("\n✓ All dependencies are satisfied!")
        print("\nYou can now run the hand gesture cursor with:")
        print("python hand_gesture_cursor.py")
    
    return True

if __name__ == "__main__":
    main()