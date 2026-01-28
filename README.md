# Learning Python Projects

This repository contains small Python projects for learning and practice purposes. It includes:

- **TalkingRobo** – a text-to-speech Python program  
- **WeatherApp** – fetch and speak current weather for a city  
- **OpenCV Image Processing** – read, display, and resize images  
- **PDF Merger** – merge multiple PDF files into a single PDF  

All projects use Python 3.x and are designed to run in a **virtual environment**.

---

## Project Structure
Learning-python/
│
├── cv-env/                  # Virtual environment (ignored by Git)
├── talkingRobo.py           # Text-to-speech robot
├── weatherApp.py            # Weather information fetcher
├── resizeImage.py           # OpenCV image resizing script
├── pdfMerger.py             # PDF merging script
├── .gitignore               # Ignored files/folders
├── requirements.txt         # Project dependencies
└── README.md                # This file

---

## Creating a Virtual Environment

It is recommended to create a separate environment for this repo:

```bash
# Navigate to project root
cd ~/Desktop/Learning-python

# Create virtual environment
python3 -m venv cv-env

# Activate environment
source cv-env/bin/activate   # macOS/Linux
# cv-env\Scripts\activate     # Windows




Install dependencies
pip install -r requirements.txt

Note: If requirements.txt is missing, you can manually install the packages:
pip install requests opencv-python pypdf2


How to Run Each Project

1️⃣ TalkingRobo
	•	Purpose: Reads text input from the user and speaks it aloud
	•	Run: python talkingRobo.py

    •	Usage:
	    •	Type any text to hear it spoken
	    •	Type q to quit

2️⃣ WeatherApp
	•	Purpose: Fetch current weather information and speak it
	•	Run: python weatherApp.py

    •	Usage:
	    •	Enter the city name
	    •	The program prints weather info and speaks the temperature and condition
	    •	Supports male/female voices (Rishi recommended for Indian English)

3️⃣ OpenCV Image Processing (resizeImage.py)
	•	Purpose: Read, display, and resize images
	•	Run:python resizeImage.py
    •	Make sure your image file (e.g., priyanshu.jpeg) is in the project folder
	•	Resized image is saved as newImage.png (or .jpg if changed)

4️⃣ PDF Merger (pdfMerger.py)
	•	Purpose: Merge multiple PDF files into a single PDF
	•	Run:python pdfMerger.py
	•	Usage:
		•	Place PDF files in the project folder
		•	Follow script instructions to select input files and output file name





Notes
	•	Virtual environments (cv-env) and input/output files (images, PDFs) are ignored by Git via .gitignore
	•	Input/output files are not tracked, so each user can use their own files
	•	Use requirements.txt to recreate the environment on another machine
	•	For macOS text-to-speech, voices like Rishi (Indian English) are recommended