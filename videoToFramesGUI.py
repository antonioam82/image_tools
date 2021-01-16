#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import Label, Button
import Pmw
import cv2
import threading
import os

class App:
    def __init__(self):

        self.ventana = Pmw.initialise(fontScheme = 'pmw1')
        self.label = Label(self.ventana,text="NO FILE SELECTED",bg='gray45',fg='white')
        self.label.pack(side='top')
        self.file = ""
        self.extract = True
        self.color = True
        self.executing = False
        self.ventana.title('VIDEO TO FRAMES')
        self.ventana.configure(bg='gray45')
        self.display = Pmw.ScrolledText(self.ventana,hscrollmode='none',
                      vscrollmode='dynamic', hull_relief='sunken',
                      hull_background='gray20', hull_borderwidth=10,
                      text_background='dark green', text_width=70,#109,
                      text_foreground='lawn green', text_height=22,#39,
                      text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
        
        self.display.pack(padx=0,pady=0)

        botones = Pmw.ButtonBox(self.ventana,hull_background="gray20")
        botones.pack(fill='both',expand=1,padx=1,pady=1)
        self.btnMode = Button(self.ventana,text="CHANGE TO GRAY MODE",width=73,bg='gray30',fg='white',command=self.mode)
        self.btnMode.pack(side='bottom')

        botones.add('SELECT VIDEO',width=23,bg='gray80',command=self.openFile)
        botones.add('EXTRACT FRAMES',width=23,bg='gray80',command=self.initExtract)
        botones.add('STOP',width=23,bg='gray80',command=self.stop_pro)
        self.display.appendtext("HELLO :)")
        botones.alignbuttons()

        self.ventana.mainloop()

    def openFile(self):
        if self.executing == False:
            self.file = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                                                   filetypes=(("mp4 files","*.mp4"),("all files","*.*")))

            if self.file != "":
                self.display.clear()
                self.archiv = self.file.split("/")[-1]
                self.name,ex = os.path.splitext(self.archiv)
                self.label.configure(text=self.archiv)
                self.display.appendtext('ROOT: {}\n'.format(self.file))

    def extractFrames(self):
        self.cam = cv2.VideoCapture(self.file)
        count = 1#0
        while(True):
            ret,frame = self.cam.read()
            if self.extract == False:
                self.display.appendtext("\nSTOPPED: {} frames generated.\n".format(count-1))
                break
            if ret:
                name = self.name+" "+str(count)+'.jpg'
                
                self.display.appendtext('Generated frame: {}\n'.format(name))
                if self.color == False:
                    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#
                    cv2.imwrite(name,gray_frame)
                else:
                    cv2.imwrite(name,frame)
                count += 1
            else:
                self.display.appendtext("\n\nPROCESS FINISHED: {} frames generated.\n".format(count-1))
                self.executing = False
                break

        self.cam.release()
        cv2.destroyAllWindows()

    def stop_pro(self):
        self.extract = False
        self.executing = False

    def mode(self):
        if self.color == True:
            self.color = False
            self.btnMode.configure(bg='light green',fg='red',text='CHANGE TO COLOR MODE')
            self.display.appendtext('\nGRAY MODE\n')
        else:
            self.color = True
            self.btnMode.configure(bg='gray30',fg='white',text='CHANGE TO GRAY MODE')
            self.display.appendtext('\nCOLOR MODE\n')

    def initExtract(self):
        if self.file != "" and self.executing == False:
            self.extract = True
            direct = filedialog.askdirectory()
            if direct != "":
                self.executing = True
                os.chdir(direct)
                t = threading.Thread(target=self.extractFrames)
                t.start()
            
if __name__=="__main__":
    App()



