from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import sys
sys.path.append('gen-py')
import face_recognition
import cv2
import mysql.connector
import sqlite3
import functools
import operator
import pickle
import time
from API import API
from API.ttypes import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    FaceRecogGUI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:

    def __init__(self, top=None):
        name = ['Sunny']
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("733x480+347+144")
        top.title("Face Recognition System")
        top.configure(background="#d9d9d9")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.505, rely=0.0, relheight=1.125)
        self.TSeparator1.configure(orient="vertical")

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.177, rely=0.042, height=31, width=94)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Cambria} -size 16 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Log In''')
        self.Label1.configure(width=94)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.737, rely=0.042, height=31, width=84)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Cambria} -size 16 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Sign Up''')
        self.Label2.configure(width=84)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.15, rely=0.5, height=34, width=127)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Read Face''', command=self.fetchInfo)
        self.Button1.configure(width=127)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.546, rely=0.208, height=21, width=38)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Name''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.546, rely=0.292, height=21, width=74)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Registration#''')
        self.Label5.configure(width=74)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.546, rely=0.375, height=21, width=45)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Semester:''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.546, rely=0.458, height=21, width=37)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''CGPA''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.682, rely=0.208, height=20, relwidth=0.224)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.682, rely=0.292, height=20, relwidth=0.224)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.682, rely=0.375, height=20, relwidth=0.224)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.682, rely=0.458, height=20, relwidth=0.224)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.628, rely=0.625, height=34, width=187)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(
            text='''Save Data and Start Training''', command=self.dbconnect)
        self.Button2.configure(width=187)

    def fetchInfo(self):
        recog = FaceRecognize(self)

    def dbconnect(self):
        name = self.Entry1.get()
        regno = self.Entry2.get()
        sem = self.Entry3.get()
        cgpa = self.Entry4.get()

        conn = sqlite3.connect('Face.db')

        c = conn.cursor()

        c.execute("INSERT into face values (?,?,?,?)",
                  (name, regno, sem, cgpa))
        conn.commit()
        conn.close()
        self.faceencode(name)

    def faceencode(self, name):
        #with open('encodings.pickle','rb') as pickle_read:
            #data = pickle.load(pickle_read)

        #encodingsBox = data['encodings']
        #namesBox = data['names']
        encodingsBox = []
        namesBox = []
        cap = cv2.VideoCapture(0)
        time.sleep(1)
        while True:
            ret, frame = cap.read()
            if ret == True:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                boxes = face_recognition.face_locations(rgb_frame, model="hog")
                encodings = face_recognition.face_encodings(rgb_frame, boxes)
                for encoding in encodings:
                    encodingsBox.append(encoding)
                    namesBox.append(name)

                cv2.imshow("Frame", frame)
                if cv2.waitKey(1) == 27 & 0xff:
                    break

        data = {'encodings': encodingsBox, 'names': namesBox}
        f = open("encodings.pickle", "wb")
        print('Hello')
        f.write(pickle.dumps(data))
        f.close()
        cap.release()
        cv2.destroyAllWindows()


class FaceRecognize():
    idNum = 0

    def __init__(self, master):
        # self.window = tk.Toplevel(root)
        # self.window.geometry("220x220")
        video_capture = cv2.VideoCapture(0)

        with open('encodings.pickle', 'rb') as pickle_read:
            data = pickle.load(pickle_read)

        knownFE = data['encodings']
        knownN = data['names']
        name = 'Pre Unknown'

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        count = 0
        while True:

            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            if process_this_frame:

                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:

                    matches = face_recognition.compare_faces(
                        knownFE, face_encoding)
                    name = "unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = knownN[first_match_index]
                        count = count+1

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) == ord('q'):
                video_capture.release()
                cv2.destroyAllWindows()
                break
        # label = tk.Label(self.window, text='Name: '+name)
        # label.pack()
        # conn = sqlite3.connect('Face.db')
        # c = conn.cursor()
        # c.execute('Select regno from face where name=?', (name,))

        # data = c.fetchone()
        # label2 = tk.Label(
        #     self.window, text='Registration Number: '+' '.join(data))
        # label2.pack()

        # c.execute('Select sem from face where name=?', (name,))

        # data = c.fetchone()
        # label3 = tk.Label(self.window, text='Semester: '+' '.join(data))
        # label3.pack()

        # c.execute('Select cgpa from face where name=?', (name,))

        # data = c.fetchone()
        # label4 = tk.Label(self.window, text='CGPA: '+' '.join(data))
        # label4.pack()

        # self.window.mainloop()
        video_capture.release()
        cv2.destroyAllWindows()
        
        try:
            transport = TSocket.TSocket('localhost', 9090)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)

            client = API.Client(protocol)

            transport.open()
            print('Connection Open')

            isEmployee = client.isOneAnEmployee(str(name))
            if(isEmployee):
                print(name + 'is an employee')
            else:
                print('Unknown Employee')
                client.reportActivity()
            
            BeHere = client.shouldOneBeHere(name, str(47))
            if(BeHere):
                print(name + 'is in valid zone')
            else:
                print('Person at invalid zone')
                client.reportActivity()

            # Close!
            transport.close()

        except Thrift.TException:
            print ('%s' % ('message'))


if __name__ == '__main__':
    vp_start_gui()
