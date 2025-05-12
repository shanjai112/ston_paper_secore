import cv2
import mediapipe as mp
import random
import time
import warnings

# Suppress specific warnings from the protobuf module
warnings.filterwarnings("ignore", category=UserWarning, module="google.protobuf")

# Initialize MediaPipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize the hand detection model
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Finger tip landmarks based on MediaPipe hands documentation
finger_tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

def detect_gesture(fingers_status):
    """Detect the gesture based on the number of fingers up."""
    if fingers_status == [0, 0, 0, 0, 0]:  # All fingers closed
        return "stone"
    elif fingers_status == [1, 1, 1, 1, 1]:  # All fingers open
        return "paper"
    elif fingers_status == [0, 1, 1, 0, 0]:  # Only index and middle fingers open
        return "scissors"
    else:
        return None  # Unknown gesture

def decide_winner(player_choice, ai_choice):
    """Decide the winner based on player's and AI's choices."""
    if player_choice == ai_choice:
        return "It's a draw!"
    elif (player_choice == "stone" and ai_choice == "scissors") or \
         (player_choice == "paper" and ai_choice == "stone") or \
         (player_choice == "scissors" and ai_choice == "paper"):
        return "You win!"
    else:
        return "AI wins!"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to avoid mirror view
    frame = cv2.flip(frame, 1)

    # Convert the frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    result = hands.process(rgb_frame)

    # Default choice for player
    player_choice = None

    # If hands are detected, process the landmarks
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks and connections on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the landmarks
            landmarks = hand_landmarks.landmark

            # List to hold whether each finger is open (1 for open, 0 for closed)
            fingers = []

            # Check for thumb (thumb moves along the x-axis compared to the index finger)
            if landmarks[finger_tips_ids[0]].x < landmarks[finger_tips_ids[0] - 1].x:
                fingers.append(1)  # Thumb is open
            else:
                fingers.append(0)  # Thumb is closed

            # Check the other four fingers (move along the y-axis)
            for tip_id in finger_tips_ids[1:]:
                if landmarks[tip_id].y < landmarks[tip_id - 2].y:
                    fingers.append(1)  # Finger is open
                else:
                    fingers.append(0)  # Finger is closed

            # Detect player's gesture based on finger positions
            player_choice = detect_gesture(fingers)

            # Display the player's gesture
            if player_choice:
                cv2.putText(frame, f'You: {player_choice}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Stone-Paper-Scissors Game', frame)

    # If 'q' is pressed, break the loop and simulate the AI's turn
    if cv2.waitKey(1) & 0xFF == ord('q') and player_choice:
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()

# Introduce a delay and then AI generates a random choice
time.sleep(2)
ai_choice = random.choice(["stone", "paper", "scissors"])

# Display AI's choice
print(f"AI: {ai_choice}")

# Decide the outcome of the game
if player_choice:
    result = decide_winner(player_choice, ai_choice)
    print(f"Result: {result}")
else:
    print("No valid gesture detected.")
