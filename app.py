import cv2
from recognition import recognize_face
from attendance import log_entry_exit
import time
import logging

def capture_image(camera_type='entry'):
    logging.info(f"تشغيل الكاميرا : {camera_type}")
    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.info("Failed to take photo")
            continue
        
        # عرض الفيديو مع التعرف على الوجوه
        employee_id = recognize_face(frame)
        if employee_id:
            print(f"Match found for employee: {employee_id}")
            if camera_type == 'entry':
                print(f"تم تسجيل دخول الموظف: {employee_id}")
                log_entry_exit(employee_id, entry_time=time.strftime('%Y-%m-%d %H:%M:%S'))
            elif camera_type == 'exit':
                print(f"تم تسجيل خروج الموظف: {employee_id}")
                log_entry_exit(employee_id, exit_time=time.strftime('%Y-%m-%d %H:%M:%S'))

        # عرض الفيديو
        cv2.imshow('Camera Feed', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    capture_image(camera_type='entry')  # Test Employee Entry
    # capture_image(camera_type='exit')  # Test Employee Exit

if __name__ == "__main__":
    main()
