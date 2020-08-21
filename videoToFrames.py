#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
import Pmw
import cv2
import os


class App:
    def __init__(self):

        self.ventana = Pmw.initialise(fontScheme = 'pmw1')

        self.display = Pmw.ScrolledText(self.ventana,hscrollmode='none',
                      vscrollmode='dynamic', hull_relief='sunken',
                      hull_background='gray20', hull_borderwidth=10,
                      text_background='black', text_width=109,
                      text_foreground='green', text_height=39,
                      text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
        
        self.display.pack(padx=0,pady=0)

        botones = Pmw.ButtonBox(self.ventana)
        botones.pack(fill='both',expand=1,padx=1,pady=1)

        botones.add('SELECT VIDEO',width=50,bg='light green',command=self.openFile)
        botones.add('EXTRACT FRAMES',width=50,bg='light green',command=self.extractFrames)

        botones.alignbuttons()

        self.ventana.mainloop()

    def openFile(self):
        file = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                filetypes=(("mp4 files","*.mp4"),("all files","*.*")))

        if file != "":
            self.cam = cv2.VideoCapture(file)

            self.display.appendtext('ROOT: {}\n'.format(file))

    def extractFrames(self):
        print(os.getcwd())
        """try:
            if not os.path.exists('video_frames'):
                os.makedirs('video_frames')

        except OSError:
            print('ERROR')"""

        count = 0
        while(True):
            self.ret,self.frame = self.cam.read()
            
            if self.ret:
                self.name = 'frame'+str(count)+'.jpg'
                self.display.appendtext('Creating...{}\n'.format(self.name))
                cv2.imwrite(self.name,self.frame)
                count += 1
            else:
                break

        self.cam.release()
        cv2.destroyAllWindows()
            
            
if __name__=="__main__":
    App()
