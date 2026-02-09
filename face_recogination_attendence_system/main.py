import cv2
from add_student import add_student_from_frame
from attendence import start_attendance  # import your attendance function

if __name__ == "__main__":
    print("Select option:")
    print("1 -> Start Attendance")
    print("2 -> Add Student")

    choice = input("Enter choice: ").strip()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    try:
        if choice == "2":
            print("Opening add-student mode...")
            add_student_from_frame(cap)  # pass the VideoCapture object directly
        elif choice == "1":
            start_attendance(cap)  # actually call your attendance function
        else:
            print("Invalid option.")

    except Exception as e:
        print(f"Application error: {e}")

    finally:
        cap.release()
        cv2.destroyAllWindows()