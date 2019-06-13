import cv2
import mqttcontroller

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

def main():
    smiling = False
    
    

    video_capture = cv2.VideoCapture(0)

    while True:
        if not smiling:
            ret, frame = video_capture.read()

            canvas, smiling = detect_smile(frame)

            cv2.imshow("Video", canvas)

            if smiling:
                mqttcontroller.send_unlock()

        if cv2.waitKey(1) & 0xff == ord("q"):
            break

def detect_smile(frame):
    smiling = False
    overlay = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(overlay, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)

        roi_gray = overlay[y:y + h, x:x + w]
        roi_colour = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.25, 45)

        for (sx, sy, sw, sh) in smiles:
            smiling = True

            # Add Rectangle and texts to canvas
            cv2.rectangle(roi_colour, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            cv2.putText(frame, "Smile detected! Unlock request sent!", (150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 120, 120), 2, cv2.LINE_AA)
            cv2.putText(frame, "Press 'Q' to quit.", (245, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 120, 120), 2, cv2.LINE_AA)
            cv2.putText(roi_colour, "Smiling!", (sx, sy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 123, 123), 1, cv2.LINE_AA)
    
    return frame, smiling

main()