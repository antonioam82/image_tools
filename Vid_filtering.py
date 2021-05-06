from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import cv2 as cv
import ffmpeg
import numpy as np
import threading
import os

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Video Filter")
        self.root.geometry("905x246")
        self.root.configure(bg="lavender")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.filename = StringVar()
        self.fpath = None
        self.element = None
        self.fr = 0
        self.nframes = 0
        self.file = None
        self.canceled = False
        self.frames_list = []
        

        Entry(self.root,textvariable=self.currentDir,width=158).place(x=0,y=0)
        Entry(self.root,textvariable=self.filename,font=('arial',23,'bold'),width=40).place(x=10,y=25)
        Button(self.root,text="SEARCH",height=2,width=25,bg="light blue1",command=self.open_file).place(x=709,y=25)
        self.btnStart = Button(self.root,text="START FILTERING",width=97,height=2,bg="light green",command=self.init_task)
        self.btnStart.place(x=8,y=77)
        Button(self.root,text="CANCEL",height=2,width=25,bg="light blue1",command=self.cancel).place(x=709,y=77)
        Label(self.root,text="FRAME RATE:",bg="lavender").place(x=709,y=150)
        self.frLabel = Label(self.root,bg='black',width=14,fg="light green")
        self.frLabel.place(x=790,y=150)
        Label(self.root,text="N FRAMES:",bg="lavender").place(x=721,y=190)
        self.nframesLabel = Label(self.root,bg='black',width=14,fg="light green")
        self.nframesLabel.place(x=790,y=190)
        self.prog_bar = ttk.Progressbar(self.root)
        self.prog_bar.place(x=10,y=170,width=687)
        self.processLabel = Label(self.root,text="PROCESS",bg="lavender",width=97)
        self.processLabel.place(x=10,y=148)

        self.root.mainloop()

    def open_file(self):
        self.file = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                        filetypes=(("mp4 files","*.mp4"),("avi files","*.avi"),("gif files","*.gif")))
        if self.file:
            self.filename.set((self.file).split("/")[-1])

            probe = ffmpeg.probe(self.file)
            self.video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
            self.fr = (self.video_streams[0]['avg_frame_rate'])
            self.nframes = (self.video_streams[0]['nb_frames'])
            self.frLabel.configure(text=self.fr)
            self.nframesLabel.configure(text=self.nframes)

    def cancel(self):
        self.canceled = True
        self.prog_bar.stop()

    def create_new_video(self):
        frame_array = []
        print(len(self.frames_list))
        for i in range(len(self.frames_list)):
            filename = self.frames_list[i]
            img = cv.imread(filename)
            height, width, layers = img.shape
            size = (width,height)

            for k in range(1):
                frame_array.append(img)
        #print(len(frame_array))

        out = cv.VideoWriter('new_video.mp4',cv.VideoWriter_fourcc(*'mp4v'), eval(self.fr), size)
        print("CREATING VIDEO...")
        C = 0
        for i in range(len(frame_array[i])):
            C+=1
            print(C)
            if C <= (len(frame_array)):
                out.write(frame_array[i])
                
        out.release()
        
        for i in self.frames_list:
            os.remove(i)
            
        print("TASK COMPLETED")

    def filtering(self):
        directory = filedialog.askdirectory()
        if directory:
            os.chdir(directory)
            self.currentDir.set(os.getcwd())
            dif = 0
            counter = 0
            self.canceled = False
            if self.file:
                self.btnStart.configure(state='disabled')
                self.cam = cv.VideoCapture(self.file)
                ret = True
                while self.canceled == False and ret:
                    ret,frame = self.cam.read()
                    if ret:
                        counter+=1
                        name = 'frame'+str(counter)+'.png'
                        blur = cv.bilateralFilter(frame,9,75,75)################
                        cv.imwrite(name,blur)##################################
                        self.frames_list.append(name)
                
                        percent = counter*100/int(self.nframes)
                        self.prog_bar.step(percent-dif)
                        self.processLabel.configure(text="PROCESSING FRAMES: {}%".format(int(percent)))
                        dif=percent
                self.create_new_video()
                self.processLabel.configure(text="PROCESS: ENDED")
                self.btnStart.configure(state='normal')
            

    def init_task(self):
        t = threading.Thread(target=self.filtering)
        t.start()

if __name__=="__main__":
    app()


