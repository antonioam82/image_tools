#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
import Pmw
import cv2
import threading
import os

class App:
    def __init__(self):

        self.ventana = Pmw.initialise(fontScheme = 'pmw1')
        self.file = ""
        self.ventana.title('VIDEO TO FRAMES')
        self.ventana.configure(bg='SeaGreen1')
        self.display = Pmw.ScrolledText(self.ventana,hscrollmode='none',
                      vscrollmode='dynamic', hull_relief='sunken',
                      hull_background='gray20', hull_borderwidth=10,
                      text_background='black', text_width=70,#109,
                      text_foreground='green', text_height=22,#39,
                      text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
        
        self.display.pack(padx=0,pady=0)

        botones = Pmw.ButtonBox(self.ventana)
        botones.pack(fill='both',expand=1,padx=1,pady=1)

        botones.add('SELECT VIDEO',width=35,bg='green yellow',command=self.openFile)
        botones.add('EXTRACT FRAMES',width=35,bg='green yellow',command=self.initExtract)

        botones.alignbuttons()

        self.ventana.mainloop()

    def openFile(self):
        self.file = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                filetypes=(("mp4 files","*.mp4"),("all files","*.*")))

        if self.file != "":
            self.cam = cv2.VideoCapture(self.file)

            self.display.appendtext('ROOT: {}\n'.format(self.file))

    def extractFrames(self):

        count = 0
        while(True):
            ret,frame = self.cam.read()
            
            if ret:
                name = 'frame'+str(count)+'.jpg'
                self.display.appendtext('Creating...{}\n'.format(name))
                cv2.imwrite(name,frame)
                count += 1
            else:
                self.display.appendtext("\n\nPROCESS FINISHED: {} frames generated\n".format(count))
                break

        self.cam.release()
        cv2.destroyAllWindows()

    def initExtract(self):
        if self.file != "":
            direct = filedialog.askdirectory()
            if direct != "":
                os.chdir(direct)
                t = threading.Thread(target=self.extractFrames)
                t.start()
            
            
if __name__=="__main__":
    App()


