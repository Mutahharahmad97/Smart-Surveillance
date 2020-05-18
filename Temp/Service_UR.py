import requests
import cv2
import json

url = 'http://localhost:8000/uniformRecognition/'

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret:
        ret, image = cv2.imencode('.jpg', frame)

        payload = {"image": image}
        r = requests.post(url, files=payload).json()

        cv2.putText(frame, r['color'], (10, r['position'][0] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, r['type'], (10, r['position'][1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        color = ((r['color'].split(':'))[0])

        cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# frame = cv2.imread('test.jpg')

# ret, image = cv2.imencode('.jpg', frame)

# payload = {"image" : image}
# r = requests.post(url, files=payload).json()

# print(r['color'])
# print(r['type'])
# print(r['position'])