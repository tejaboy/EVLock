import cv2
import paho.mqtt.client as mqtt

import mqttcontroller

# We retrieve the prebuilt cascade so we can use it to detect a face and smile.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

def main():
    # Connect the MQTT client to the mosquitto server
    client = mqtt.Client()
    mqttcontroller.connect(client)

    # This opens up a new window to begin capturing with your WebCam
    video_capture = cv2.VideoCapture(0)

    # We will loop this program until a `break` is detected.
    while True:
        # We will read the video feed.
        ret, frame = video_capture.read()

        # And pass it to the detect_smile() function.
        # Returned values are edited frame (overlay text, rectangle etc).
        canvas, smiling = detect_smile(frame)

        # We show the edited frame to the user
        # for debugging purposes (or maybe "WOW" factor).
        cv2.imshow("Video", canvas)

        if smiling:
            mqttcontroller.send_unlock(client)
            break

        if cv2.waitKey(1) & 0xff == ord("q"):
            break


def detect_smile(frame):
    # We first set the local variable `smile` to False.
    smiling = False
    # Then we convert the frame to grayscale - easier for OpenCV to process
    overlay = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Here we make use of `face_cascade` to detect faces.
    faces = face_cascade.detectMultiScale(overlay, 1.3, 5)

    for (x, y, w, h) in faces:
        # For every faces that we detected, we draw a rectangle over it.
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)

        # Split the face rectangle to two different types - grayscale and color
        # Grayscale: Allow OpenCV to detect smile better.
        # Color: Add another rectangle over the smile and
        # return it to the main frame.
        roi_gray = overlay[y:y + h, x:x + w]
        roi_colour = frame[y:y + h, x:x + w]

        # We then make use of the `smile_cascade` to
        # detect smiles within the face.
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.25, 45)

        for (sx, sy, sw, sh) in smiles:
            # If a smile is detected, we will set the `smiling` (local) to True
            smiling = True

            # Add Rectangle and Texts to colored canvas
            cv2.rectangle(
                roi_colour, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            cv2.putText(
                roi_colour, "Smiling!", (sx, sy), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 123, 123), 1, cv2.LINE_AA)
            cv2.putText(
                frame, "Smile detected! Unlock request sent!", (150, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 120, 120), 2, cv2.LINE_AA)
            cv2.putText(
                frame, "Press 'Q' to quit.", (245, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 120, 120), 2, cv2.LINE_AA)

    # Finally, we will return `smiling` to the caller.
    return frame, smiling

main()