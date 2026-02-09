import cv2
import face_recognition
import os
import pickle

STUDENT_IMAGE_FOLDER = "students_image"
ENCODING_FOLDER = "face_encodings"

def add_student_from_frame(cap):
    try:
        if cap is None or not cap.isOpened():
            print("Error: Camera not available.")
            return

        print("Press SPACE to capture student face. Press 'q' to cancel.")

        captured_frame = None

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read frame from camera.")
                return

            preview_frame = frame.copy()
            cv2.putText(
                preview_frame,
                "Press SPACE to capture | Q to cancel",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )
            cv2.imshow("Add Student", preview_frame)

            key = cv2.waitKey(1) & 0xFF

            if key == 32:  # SPACE key
                captured_frame = frame
                break

            if key == ord('q'):
                cv2.destroyWindow("Add Student")
                print("Student add cancelled.")
                return

        cv2.destroyWindow("Add Student")

        if captured_frame is None:
            print("No frame captured.")
            return

        student_name = input("Enter student name: ").strip()
        if student_name == "":
            print("Invalid name.")
            return

        rgb_frame = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        if len(face_locations) == 0:
            print("No face detected. Try again.")
            return

        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        if len(face_encodings) == 0:
            print("Encoding failed. Try again.")
            return

        encoding = face_encodings[0]

        os.makedirs(STUDENT_IMAGE_FOLDER, exist_ok=True)
        os.makedirs(ENCODING_FOLDER, exist_ok=True)

        image_path = os.path.join(STUDENT_IMAGE_FOLDER, f"{student_name}.jpg")
        cv2.imwrite(image_path, captured_frame)

        encoding_path = os.path.join(ENCODING_FOLDER, f"{student_name}.pkl")
        with open(encoding_path, "wb") as f:
            pickle.dump(encoding, f)

        print(f"Student '{student_name}' added successfully.")

    except Exception as e:
        print(f"Critical error while adding student: {e}")
