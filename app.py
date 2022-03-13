from flask import Flask, render_template, Response
import cv2
from deepface import DeepFace


app=Flask(__name__)
camera = cv2.VideoCapture(0)

def emotion_check(expression):

    show = ""
    
    if expression == 'happy':
        show = "Hey, That's an absolutely beautiful smile"
    
    elif expression == 'sad':
        show = 'Say Cheese!!'
    
    elif expression == 'neutral':
        show = 'Wide SMILE :) !!'
    
    elif expression == 'disgust':
        show = "Say EEEEEEEEEEEEE"

    elif expression == 'angry':
        show = 'Show us that beautiful smile of yours'
    
    elif expression == 'fear':
        show = 'Want to talk about something?'

    elif expression == 'Surprise':
        show = 'Surprisee!!!!'        
    return show

def generate_frames():  
    while True:
        success, frame = camera.read()  
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            result = DeepFace.analyze(frame, actions = ['emotion'], enforce_detection=False)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_TRIPLEX

            display = emotion_check(result['dominant_emotion'])
            cv2.putText(frame, display, (0, 50), font, 1, (0, 0, 255), 2, cv2.LINE_4)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=='__main__':
    app.run(debug=True)