import csv
import os
from datetime import datetime as dt
import cv2
import face_recognition
import pickle


# ===============================
# MARK ATTENDANCE
# ===============================
def mark_attendance(name):
    try:
        # normalize name
        name = name.strip().lower().replace(" ", "_")

        folder_name = "daily_attendance"
        os.makedirs(folder_name, exist_ok=True)

        now = dt.now()
        date_string = now.strftime('%Y-%m-%d')
        time_string = now.strftime('%H:%M:%S')

        file_path = os.path.join(folder_name, f"{date_string}.csv")

        already_marked = False

        # Read existing names
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader, None)  # skip header
                for row in reader:
                    if len(row) > 0 and row[0] == name:
                        already_marked = True
                        break

        # Write only if not marked
        if not already_marked:
            file_exists = os.path.exists(file_path)

            with open(file_path, 'a', newline='') as f:
                writer = csv.writer(f)

                # add header if new file
                if not file_exists:
                    writer.writerow(["name", "date", "time"])

                writer.writerow([name, date_string, time_string])

            print(f"Attendance marked for {name}")

    except Exception as e:
        print("Error marking attendance:", e)


# ===============================
# LOAD ENCODINGS
# ===============================
def load_known_encodings():
    known_encodings = []
    known_names = []

    encoding_folder = "face_encodings"

    try:
        if not os.path.exists(encoding_folder):
            print("Encoding folder not found.")
            return known_encodings, known_names

        for file in os.listdir(encoding_folder):
            if file.endswith(".pkl"):
                path = os.path.join(encoding_folder, file)

                with open(path, "rb") as f:
                    encoding = pickle.load(f)

                name = os.path.splitext(file)[0]

                known_encodings.append(encoding)
                known_names.append(name)

        print(f"Loaded {len(known_names)} known faces.")

    except Exception as e:
        print("Error loading encodings:", e)

    return known_encodings, known_names


# ===============================
# START ATTENDANCE
# ===============================
def start_attendance(cap):

    try:
        known_encodings, known_names = load_known_encodings()

        if len(known_encodings) == 0:
            print("No student encodings found.")
            return

        print("Attendance started. Press 'q' to quit.")

        while True:

            ret, frame = cap.read()

            if not ret:
                print("Failed to read from camera.")
                break

            # Resize for speed (VERY important optimization)
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small)
            face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):

                name = "Unknown"

                if len(known_encodings) > 0:

                    # Better matching using face distance
                    distances = face_recognition.face_distance(
                        known_encodings,
                        face_encoding
                    )

                    best_match_index = distances.argmin()

                    if distances[best_match_index] < 0.5:
                        name = known_names[best_match_index]
                        mark_attendance(name)

                # Draw box (scaled back to original frame size)
                top, right, bottom, left = face_location
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                cv2.putText(frame, name, (left, top-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (0,255,0), 2)

                

            cv2.imshow("Attendance", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Attendance system error:", e)

    finally:
        cap.release()
        cv2.destroyAllWindows()