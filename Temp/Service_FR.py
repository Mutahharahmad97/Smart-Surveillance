import requests
import cv2
import json

url = 'http://localhost:8000/faceRecognition/'

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    if ret:
        ret, image = cv2.imencode('.jpg', frame)
        
        payload = {"image": image}
        r = requests.post(url, files=payload).json()
        
        for(name,title,top,right,bottom,left) in r['faces']:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name+ ": " + title, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            
        cv2.imshow('Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
