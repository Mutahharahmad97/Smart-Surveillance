import face_recognition
import sys
import cv2
import pickle
from MainPage import *
from FaceRecognition import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from API import API
from API.ttypes import *

class MainWindow(QtWidgets.QMainWindow):
    def exit_(self):
        sys.exit()
        cv2.destroyAllWindows()
        
    def nextFrameSlot(self):
        process_this_frame = True
        ret, frame = self.vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(knownFE, face_encoding)
            name = "Not In Database"

            if True in matches:
                first_match_index = matches.index(True)
                name = knownN[first_match_index]

            face_names.append(name)
            
        process_this_frame = not process_this_frame
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        #self.ui.label_4.setText(str(face_names[0]))
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.ui.label.setPixmap(pixmap)
        
    def FRWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Face_Recognition_Window()
        self.ui.setupUi(self.window)
        self.window.show()
        
        self.vc = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./24)
        #self.vc.release()
        
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        
        self.ui = Main_Window()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.FRWindow)
        self.ui.pushButton_2.clicked.connect(self.FRWindow)
        self.ui.pushButton_3.clicked.connect(self.exit_)


global knownFE
global knownN
with open('C:/Users/SHAKH/Documents/VS Code/Smart Surveilliance/Python/UI/encodings.pickle', 'rb') as pickle_read:
    data = pickle.load(pickle_read)

knownFE = data['encodings']
knownN = data['names']

app = QtWidgets.QApplication(sys.argv)
myApp = MainWindow()
myApp.show()
sys.exit(app.exec_())
