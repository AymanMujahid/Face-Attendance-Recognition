import face_recognition
import cv2

def recognize_face(image):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    if len(face_encodings) > 0:
        employee_id = match_face_with_employee(face_encodings[0])

        if employee_id:
            for face_location in face_locations:
                draw_face_mask(image, face_location, employee_id)
            return employee_id
    else:
        print("No faces detected.")
        return None

def draw_face_mask(image, face_location, employee_name):
    top, right, bottom, left = face_location
    
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    
    cv2.putText(image, employee_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


def match_face_with_employee(face_encoding):
    known_employee_encodings = load_known_faces() 
    employee_ids = list(known_employee_encodings.keys())

    matches = face_recognition.compare_faces(list(known_employee_encodings.values()), face_encoding)
    
    if True in matches:
        match_index = matches.index(True)
        print(f"Match found for employee: {employee_ids[match_index]}")
        return employee_ids[match_index] 
    else:
        print("No match found for the provided face encoding.")
        return None

def load_known_faces():
    known_face_encodings = {}
    employee_images = {
        "Ahmed_muhammed" : "C:\\FaceRecognation\\data\\h01.jpeg",
        "Mustafa_Ashraf" : "C:\\FaceRecognation\\data\\h02.jpeg",
        "Hazem_AbdElstar": "C:\\FaceRecognation\\data\\h03.jpeg",
        "Muhammed_Osama" : "C:\\FaceRecognation\\data\\h04.jpeg",
        "Ayman_badr"     : "C:\\FaceRecognation\\data\\h05.jpeg",
        "Amer_fariid"    : "C:\\FaceRecognation\\data\\h06.jpeg",

    }
    
    for employee_id, image_path in employee_images.items():
        try:
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            if face_encodings:
                encoding = face_encodings[0]  
                known_face_encodings[employee_id] = encoding
            else:
                print(f"No faces found in image for employee: {employee_id}")
        except Exception as e:
            print(f"Error loading image for {employee_id}: {e}")
    
    return known_face_encodings
