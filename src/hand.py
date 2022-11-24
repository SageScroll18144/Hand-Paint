import cv2
import mediapipe as mp
import math
import pygame as pg

BLACK = (0,0,0)

screen = pg.display.set_mode((1200,800))
screen.fill((255,255,255))

WINDOW_NAME = "bora billl"

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def drawCircle(screen, x, y):
  pg.draw.circle( screen, BLACK, ( x, y ), 10 )

def euclian_distance(x,y,z):
  #print((math.sqrt(x**2+y**2+z**2)))
  return (math.sqrt(x**2+y**2+z**2)) <= 0.17

isPressed = False
flag = False
sum_x = 0
sum_y = 0

# For webcam input:
cap = cv2.VideoCapture(0)

list_of_the_fingers = [8, 12, 16, 20]

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      #print([
      #print(results.multi_hand_landmarks[0])
      for i in list_of_the_fingers:
        if euclian_distance(results.multi_hand_landmarks[0].landmark[4].x - results.multi_hand_landmarks[0].landmark[i].x, results.multi_hand_landmarks[0].landmark[4].y - results.multi_hand_landmarks[0].landmark[i].y, results.multi_hand_landmarks[0].landmark[4].z - results.multi_hand_landmarks[0].landmark[i].z):
          flag = True
        else:
          flag = False
          break
      for i in range(21):
        sum_x+=results.multi_hand_landmarks[0].landmark[i].x
        sum_y+=results.multi_hand_landmarks[0].landmark[i].y

      sum_x = (sum_x/21)
      sum_y = (sum_y/21)
      if flag:
        #print("PINTANDO")
        drawCircle(screen, (1 - sum_x) * 1200, sum_y * 800)
      #else: 
        #print("AGORA NAOO")
        
      print(results.multi_hand_landmarks[0].landmark[8].z)
    # Flip the image horizontally for a selfie-view display.
    # cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(WINDOW_NAME, cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
    pg.display.flip()

cap.release()
pg.quit()
