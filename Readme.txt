Stone-Paper-Scissors Gesture Game
=================================

Description:
------------
This Python script allows you to play the classic Stone-Paper-Scissors game using hand gestures via your webcam. 
It uses OpenCV for video capture and MediaPipe for hand tracking and gesture recognition.

Features:
---------
- Detects your hand gesture in real time using webcam
- Recognizes 3 gestures: Stone (fist), Paper (open hand), Scissors (index and middle fingers)
- AI randomly selects its move after you quit
- Displays winner in the terminal

Requirements:
-------------
- Python 3.x
- Required Python Libraries:
  - opencv-python
  - mediapipe

Install the required packages using pip:
    pip install opencv-python mediapipe

Usage:
------
1. Run the script:
       python ston_paper_secore.py

2. The webcam window will open. Show one of the following hand gestures:
   - Fist (Stone)
   - Open Hand (Paper)
   - Index + Middle Fingers (Scissors)

3. Press the 'q' key to lock your gesture and allow the AI to make its move.

4. The AI will choose randomly and the result will be printed in the terminal.

Gesture Mapping:
----------------
- Stone    -> All fingers closed
- Paper    -> All fingers open
- Scissors -> Only index and middle fingers open

Legal Notice:
-------------
Use this program responsibly. It captures video from your webcam for gesture detection only.
No data is stored or transmitted.

Disclaimer:
-----------
This game is provided for educational and entertainment purposes.
The author is not responsible for any misuse or hardware issues.
