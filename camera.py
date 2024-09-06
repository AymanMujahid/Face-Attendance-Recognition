import cv2
import logging

def capture_image(camera_type):
    
    camera_index = 0
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        logging.info("Error: Could not open camera.")
        return None
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None
