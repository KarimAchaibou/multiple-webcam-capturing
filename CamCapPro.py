# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:26:18 2017

@author: BEKAH

versie 2
"""

import cv2
import datetime
import os
import numpy as np

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import threading
#☺from datetime import datetime

#test=Tk()
root=tkinter.Tk()
root.title("Camera Capturing Program - bekah")

nb = ttk.Notebook(root)
nb.pack()
tab1 = tkinter.Frame(nb)   # first page, which would get widgets gridded into it
tab2 = tkinter.Frame(nb)   # second page
nb.add(tab1, text='Making Pictures of cams')
nb.add(tab2, text='Making Movies from pictures')

nb.select(tab1)
nb.enable_traversal()

#functions:

def start_runProgram_thread(event):
#    print("in thread methode 1 ")
    global runProgram_thread
#    progressbar.start
    runProgram_thread = threading.Thread(target=runProgramTakePictures)
    runProgram_thread.daemon = True
#    print("in thread methode 2 ")
    #progressbar.start
    runProgram_thread.start()
    root.after(20, check_runProgram_thread)

def check_runProgram_thread():
    if runProgram_thread.is_alive():
        root.after(20, check_runProgram_thread)
    else:
#        progressbar.stop
        printToFeedbackWindow("Program stopped")
        print("Program stopped")
        

def delete_start_frame_data():
#    filepathStartFolderTextFrame.delete("1.0",END)
    camTFStart.delete("1.0",END)
    jaarTFStart.delete("1.0",END)        
    maandTFStart.delete("1.0",END)        
    dagTFStart.delete("1.0",END)       
    uurTFStart.delete("1.0",END)        
    minTFStart.delete("1.0",END)        
    secTFStart.delete("1.0",END)        
    msecTFStart.delete("1.0",END)
    extTFStart.delete("1.0",END)

def delete_end_frame_data():
    camTFEnd.delete("1.0",END)
    jaarTFEnd.delete("1.0",END)        
    maandTFEnd.delete("1.0",END)        
    dagTFEnd.delete("1.0",END)       
    uurTFEnd.delete("1.0",END)        
    minTFEnd.delete("1.0",END)        
    secTFEnd.delete("1.0",END)        
    msecTFEnd.delete("1.0",END)
    extTFEnd.delete("1.0",END)

def insert_start_frame_data(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext):
    camTFStart.insert(END,cam)
    jaarTFStart.insert(END,jaar)        
    maandTFStart.insert(END,maand)        
    dagTFStart.insert(END,dag)       
    uurTFStart.insert(END,uur)        
    minTFStart.insert(END,minuten)        
    secTFStart.insert(END,sec)        
    msecTFStart.insert(END,microsec)
    extTFStart.insert(END,ext)

def insert_end_frame_data(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext):    
    camTFEnd.insert(END,cam)
    jaarTFEnd.insert(END,jaar)        
    maandTFEnd.insert(END,maand)        
    dagTFEnd.insert(END,dag)       
    uurTFEnd.insert(END,uur)        
    minTFEnd.insert(END,minuten)        
    secTFEnd.insert(END,sec)        
    msecTFEnd.insert(END,microsec)
    extTFEnd.insert(END,ext)
        
def saveDir(pos):
    if pos == 0:
        #window.withdraw()  #hiden van main window
        filepathTextFrame.delete("1.0",END)
        filepath = filedialog.askdirectory()
        filepathTextFrame.insert(END,filepath)  
        printToFeedbackWindow(filepath)
        #window.deiconify()   #terug tonen main window
        #print(filepath)
    elif pos == 1:
        delete_start_frame_data()
        delete_end_frame_data()
        filepathStartFolderTextFrame.delete("1.0",END)
#        camTFStart.delete("1.0",END)
#        jaarTFStart.delete("1.0",END)        
#        maandTFStart.delete("1.0",END)        
#        dagTFStart.delete("1.0",END)       
#        uurTFStart.delete("1.0",END)        
#        minTFStart.delete("1.0",END)        
#        secTFStart.delete("1.0",END)        
#        msecTFStart.delete("1.0",END)
#        extTFStart.delete("1.0",END)
        
#        camTFEnd.delete("1.0",END)
#        jaarTFEnd.delete("1.0",END)        
#        maandTFEnd.delete("1.0",END)        
#        dagTFEnd.delete("1.0",END)       
#        uurTFEnd.delete("1.0",END)        
#        minTFEnd.delete("1.0",END)        
#        secTFEnd.delete("1.0",END)        
#        msecTFEnd.delete("1.0",END)
#        extTFEnd.delete("1.0",END)
        
        fileName = filedialog.askopenfilename()
        path = os.path.dirname(fileName)
        file = str(fileName).split("/")[-1]
#        print(file)
        cam,jaar,maand,dag,uur,minuten,sec,microsec = file.split("_")
        microsec = microsec.split(".")[0]
        ext = os.path.splitext(os.path.abspath(fileName))[1]
        
#        print(cam,jaar,maand,dag,uur,minuten,sec,microsec)

        filepathStartFolderTextFrame.insert(END,path) 
        insert_start_frame_data(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext)
        insert_end_frame_data(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext)
#        camTFStart.insert(END,cam)
#        jaarTFStart.insert(END,jaar)        
#        maandTFStart.insert(END,maand)        
#        dagTFStart.insert(END,dag)       
#        uurTFStart.insert(END,uur)        
#        minTFStart.insert(END,minuten)        
#        secTFStart.insert(END,sec)        
#        msecTFStart.insert(END,microsec)
#        extTFStart.insert(END,ext)
#        
#        camTFEnd.insert(END,cam)
#        jaarTFEnd.insert(END,jaar)        
#        maandTFEnd.insert(END,maand)        
#        dagTFEnd.insert(END,dag)       
#        uurTFEnd.insert(END,uur)        
#        minTFEnd.insert(END,minuten)        
#        secTFEnd.insert(END,sec)        
#        msecTFEnd.insert(END,microsec)
#        extTFEnd.insert(END,ext)
        
        printToFeedbackWindow(fileName)
        #window.deiconify()   #terug tonen main window
        #print(fileName)
    elif pos == 2:
        filepathEndPicTextFrame.delete("1.0",END)
        fileName = filedialog.askopenfilename()
        filepathEndPicTextFrame.insert(END,fileName)  
        printToFeedbackWindow(fileName)
        #window.deiconify()   #terug tonen main window
        #print(fileName)
    elif pos == 3:
        filepathOutputDirTextFrame.delete("1.0",END)
        filepath = filedialog.askdirectory()
        filepathOutputDirTextFrame.insert(END,filepath)  
        printToFeedbackWindow(filepath)
        #window.deiconify()   #terug tonen main window
        #print(filepath)
#    elif pos == 4:
#        filepathStartFolderTextFrame.delete("1.0",END)
#        filepath = filedialog.askdirectory()
#        print(filepath)
#        first_file = next(join(filepath, f) for f in os.listdir(filepath) if isfile(join(filepath, f)))
#        print(first_file)
#        
#        filepathStartFolderTextFrame.insert(END,filepath)  
#        printToFeedbackWindow(filepath)

def rotate90(camNumber):
    feedbackTextFrame.delete("1.0",END)
    feedbackTextFrame.insert(END,"rotating cam %s 90°" %camNumber)
#    messagebox.showerror("Error", "Error message")
#    messagebox.showwarning("Warning","Warning message")
#    messagebox.showinfo("Information","Informative message")
    
def flip(camNumber):
    feedbackTextFrame.delete("1.0",END)
    feedbackTextFrame.insert(END,"flipping cam %s 90°" %camNumber)

def showCam(camNumber,waitingTime=5000):    
    window.withdraw()
    print(rotCam1.get())
#    print("in showCam functie 1")  
#    print(camNumber)
 
    cam = cv2.VideoCapture(camNumber)
    ret, frame = cam.read()
    if ret:
        print("in showCam functie 2")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        rotCam = 0
        flipCam = 0
        if camNumber == 1:
            rotCam = rotCam1.get()
            flipCam = flipCam1.get()
        elif camNumber == 2:
            rotCam = rotCam2.get()
            flipCam = flipCam2.get()            
        elif camNumber == 3:
            rotCam = rotCam3.get()
            flipCam = flipCam3.get()           
        elif camNumber == 4:
            rotCam = rotCam3.get()
            flipCam = flipCam3.get()
           
        if rotCam == 1:
            gray = np.rot90(gray)
        if flipCam == 1:
            gray = np.flip(gray,0)
            
        cv2.imshow('webcam %s' %camNumber,gray)         
    if not ret or cv2.waitKey(waitingTime) or 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
#        print("destroyed")
        exit #break
    window.deiconify()

def makeDir(numberOfCams,directory):
#    print("in makeDir()")
    i=1
    while numberOfCams >= i:
        directoryCam = directory + '/cam' + str(i)
        if not os.path.exists(directoryCam):
            os.makedirs(directoryCam)
        i+=1

def printToFeedbackWindow(text):
    feedbackTextFrame.delete("1.0",END)
    feedbackTextFrame.insert(END,text)

def getTimeStamp():
    now = datetime.datetime.now()
    tm_year = now.year
    tm_mon  = now.month
    tm_day = now.day
    tm_hour = now.hour
    tm_min = now.minute
    tm_sec = now.second
    tm_mil = now.microsecond
    
    if tm_mon < 10: tm_mon = '0'+ str(tm_mon)
    if tm_day < 10: tm_day = '0'+ str(tm_day)
    if tm_hour < 10: tm_hour = '0'+ str(tm_hour)
    if tm_min < 10: tm_min = '0'+ str(tm_min)
    if tm_sec < 10: tm_sec = '0'+ str(tm_sec)
        
    timestamp = str(tm_year) + "_" + str(tm_mon)  + "_" + str(tm_day) + "_" + str(tm_hour) + "_" + str(tm_min) + "_" + str(tm_sec) + "_" + str(tm_mil)
    printToFeedbackWindow(timestamp)
    return timestamp       

    
def runProgramTakePictures():
#    print("in run program")
    directory = filepathTextFrame.get("1.0",'end-1c')  #filepathTextFrame.get("1.0",END)
    numberOfCams = Entry_numOfCams_value.get()
    timeBetweenFrames = int(Entry_timeBetweenFrames_value.get())
    
    print("Module: take pictures from cameras")
    print("numberOfCams: %s" %numberOfCams)
    print("output dir: %s" %directory)
    print("timeBetweenFrames: %sms" %timeBetweenFrames)
    
    #check if directory was selected; number of cameras was filled in
    if directory == "":
        messagebox.showerror("Error", "No file path available")
        exit
        
    if numberOfCams == "":
        messagebox.showerror("Error", "Number of cameras not defined")
        exit
    else:
        numberOfCams = int(numberOfCams)
    
    #create dir's cam1 ... cam4 under the selected dir
    makeDir(numberOfCams,directory)
    
    lbl_quit_value.set('Press "q" to quit in view')
    
    #creat VideoCapture objects and put them in list cam[]
    cam=[]
    i = 1
    while numberOfCams >= i:     
        cam.append(cv2.VideoCapture(i))
        i+=1   
            
#    i = 1
    while(True):
        #get the current time
        timestamp = getTimeStamp()   
        # Capture frame-by-frame
        j = 1
        while numberOfCams >= j:
            ret, frame = cam[j-1].read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if j == 1:
                    if rotCam1.get() == 1:
                        gray = np.rot90(gray)
                    if flipCam1.get() == 1:
                        gray = np.flip(gray,0)      
                elif j == 2:
                    if rotCam2.get() == 1:
                        gray = np.rot90(gray)
                    if flipCam2.get() == 1:
                        gray = np.flip(gray,0)                
                elif j == 3:
                    if rotCam3.get() == 1:
                        gray = np.rot90(gray)
                    if flipCam3.get() == 1:
                        gray = np.flip(gray,0)                     
                elif j == 4:
                    if rotCam4.get() == 1:
                        gray = np.rot90(gray)
                    if flipCam4.get() == 1:
                        gray = np.flip(gray,0)  
        
                cv2.imwrite('{value1}/cam{value2}/cam{value3}_{value4}.png'.format(value1 = directory,value2 = j,value3 = j,value4 = timestamp),gray)
                cv2.imshow('webcam_%s' %j,gray)   
            j += 1 

        if cv2.waitKey(timeBetweenFrames) & 0xFF == ord('q'):
            lbl_quit_value.set('')
            break 

    # When everything done, release the capture
    for cams in cam:
        cams.release()    
   
    cv2.destroyAllWindows()


def dryRun():
    global StartFrame
    global StopByEndFrame
    StartFrame = False
    StopByEndFrame = False
#    check if directory is given
    dir_path_startPic = filepathStartFolderTextFrame.get("1.0",'end-1c')
    if dir_path_startPic == "":
        printToFeedbackWindow("Select start Picture")
        return  #exit def
    else:
        dir_path_startPic = filepathStartFolderTextFrame.get("1.0",'end-1c')+"/"
        
    fps = int(Entry_fps_value.get())
    print(fps)

    camStart = camTFStart.get("1.0",'end-1c')
    jaarStart = int(jaarTFStart.get("1.0",'end-1c'))
    maandStart = int(maandTFStart.get("1.0",'end-1c'))
    dagStart = int(dagTFStart.get("1.0",'end-1c'))
    uurStart = int(uurTFStart.get("1.0",'end-1c'))
    minStart = int(minTFStart.get("1.0",'end-1c'))
    secStart = int(secTFStart.get("1.0",'end-1c'))
    msecStart = int(msecTFStart.get("1.0",'end-1c'))      
    
    startTimestamp=datetime.datetime(jaarStart,maandStart,dagStart,uurStart,minStart,secStart,msecStart)

    camEnd = camTFEnd.get("1.0",'end-1c')
    jaarEnd = int(jaarTFEnd.get("1.0",'end-1c'))
    maandEnd = int(maandTFEnd.get("1.0",'end-1c'))
    dagEnd = int(dagTFEnd.get("1.0",'end-1c'))
    uurEnd = int(uurTFEnd.get("1.0",'end-1c'))
    minEnd = int(minTFEnd.get("1.0",'end-1c'))
    secEnd = int(secTFEnd.get("1.0",'end-1c'))
    msecEnd = int(msecTFEnd.get("1.0",'end-1c'))  
    
    endTimestamp=datetime.datetime(jaarEnd,maandEnd,dagEnd,uurEnd,minEnd,secEnd,msecEnd)
    
    ext = extTFStart.get("1.0",'end-1c') 
 
    if startTimestamp == "" or endTimestamp == "":
        printToFeedbackWindow("select start and end time")
        exit
    else:  
        #namen van de files in array images plaatsen
        frame = ""
        images = []
        i = 0
        for f in os.listdir(dir_path_startPic):
            file = str(f).split("/")[-1]
            camCur,jaarCur,maandCur,dagCur,uurCur,minutenCur,secCur,microsecCur = file.split("_")
            microsecCur = microsecCur.split(".")[0]
#            ext = os.path.splitext(os.path.abspath(fileName))[1]
            timestampCurrentPic = datetime.datetime(int(jaarCur),int(maandCur),int(dagCur),int(uurCur),int(minutenCur),int(secCur),int(microsecCur))
#            print('current time %s:' %timestampCurrentPic)
            if f.endswith(ext):
                if timestampCurrentPic >= startTimestamp:
                    if timestampCurrentPic <= endTimestamp:
                        if i == 0:
                            # Determine the width and height from the first image
                            frame = cv2.imread(dir_path_startPic + "/" + f)
                            #cv2.imshow('video',frame)
                            height, width, channels = frame.shape
                            #print(height, width, channels)
                            i = i + 1
                        images.append(f)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    for image in images:

        timeStamp = image
        image_path = os.path.join(dir_path_startPic, image)
        frame = cv2.imread(image_path)    
        frame = cv2.putText(frame,timeStamp,(2,25),font,0.7,(0,255,255),2,cv2.LINE_AA)    
    
        cv2.imshow('Select left mousse button to define start and end frame',frame)
        cv2.setMouseCallback('Select left mousse button to define start and end frame', click_and_select_start_frame,param=image)
        if (cv2.waitKey(fps) & 0xFF) == ord('q') or StopByEndFrame == True: # Hit `q` to exit
            break
    
    # Release everything if job is finished
#    out.release()
    cv2.destroyAllWindows()       
    
def makeMovieFromPictures():
    fps = int(Entry_fps_value.get())
    
    #get start en end picture path en filename
    outputDir = filepathOutputDirTextFrame.get("1.0",'end-1c')
    outputfileName = outputDir + '/' +  Entry_movieName_value.get() + '.mp4'
#    print("output dir: ", outputDir)
#    print(outputfileName)
#    camTFStart_value
    
    camStart = camTFStart.get("1.0",'end-1c')
    jaarStart = int(jaarTFStart.get("1.0",'end-1c'))
    maandStart = int(maandTFStart.get("1.0",'end-1c'))
    dagStart = int(dagTFStart.get("1.0",'end-1c'))
    uurStart = int(uurTFStart.get("1.0",'end-1c'))
    minStart = int(minTFStart.get("1.0",'end-1c'))
    secStart = int(secTFStart.get("1.0",'end-1c'))
    msecStart = int(msecTFStart.get("1.0",'end-1c'))      
    
    startTimestamp=datetime.datetime(jaarStart,maandStart,dagStart,uurStart,minStart,secStart,msecStart)
    dir_path_startPic = filepathStartFolderTextFrame.get("1.0",'end-1c')+"/"
#    print("dir_path_startPic: %s" %dir_path_startPic)

    camEnd = camTFEnd.get("1.0",'end-1c')
    jaarEnd = int(jaarTFEnd.get("1.0",'end-1c'))
    maandEnd = int(maandTFEnd.get("1.0",'end-1c'))
    dagEnd = int(dagTFEnd.get("1.0",'end-1c'))
    uurEnd = int(uurTFEnd.get("1.0",'end-1c'))
    minEnd = int(minTFEnd.get("1.0",'end-1c'))
    secEnd = int(secTFEnd.get("1.0",'end-1c'))
    msecEnd = int(msecTFEnd.get("1.0",'end-1c'))  
    
    endTimestamp=datetime.datetime(jaarEnd,maandEnd,dagEnd,uurEnd,minEnd,secEnd,msecEnd)
    
    ext = extTFStart.get("1.0",'end-1c') 
#    dir_path_endPic = camTFStart_value.get()    
#    dir_path_startPic,startPic = os.path.split(os.path.abspath(filepathStartPicTextFrame.get("1.0",'end-1c')))
#    dir_path_endPic,endPic = os.path.split(os.path.abspath(filepathEndPicTextFrame.get("1.0",'end-1c')))
#    #get the extension of the file name => eg. .png, .jpg
#    ext = os.path.splitext(os.path.abspath(filepathStartPicTextFrame.get("1.0",'end-1c')))[1]
#    print(ext)
    
#    print(dir_path_startPic,startPic)
#    print(dir_path_endPic,endPic)
    print("module: make movie from pictures") 
    print('Start time: %s' %startTimestamp)
    print('End time: %s' %endTimestamp)
    print('fps: %s' %fps)
    print('Output dir: %s' %outputDir)     
    
    if startTimestamp == "" or endTimestamp == "":
        printToFeedbackWindow("select start and end time")
        exit
    else:  
        #namen van de files in array images plaatsen
        frame = ""
        images = []
        i = 0
        for f in os.listdir(dir_path_startPic):
            file = str(f).split("/")[-1]
            camCur,jaarCur,maandCur,dagCur,uurCur,minutenCur,secCur,microsecCur = file.split("_")
            microsecCur = microsecCur.split(".")[0]
#            ext = os.path.splitext(os.path.abspath(fileName))[1]
            timestampCurrentPic = datetime.datetime(int(jaarCur),int(maandCur),int(dagCur),int(uurCur),int(minutenCur),int(secCur),int(microsecCur))
#            print('current time %s:' %timestampCurrentPic)
            if f.endswith(ext):
                if timestampCurrentPic >= startTimestamp:
                    if timestampCurrentPic <= endTimestamp:
                        if i == 0:
                            # Determine the width and height from the first image
                            frame = cv2.imread(dir_path_startPic + "/" + f)
                            #cv2.imshow('video',frame)
                            height, width, channels = frame.shape
                            #print(height, width, channels)
                            i = i + 1
                        images.append(f)
        print('Number of images loaded %s:' %len(images))                

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(outputfileName, fourcc, fps, (width, height))
    
    #row,col = images.size()
    
    #print row,col
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    for image in images:
#        print(image)
        timeStamp = image
        image_path = os.path.join(dir_path_startPic, image)
        frame = cv2.imread(image_path)    
        frame = cv2.putText(frame,timeStamp,(2,25),font,0.7,(0,255,255),2,cv2.LINE_AA)
    
        out.write(frame) # Write out frame to video
    
        cv2.imshow('video',frame)
        if (cv2.waitKey(10) & 0xFF) == ord('q'): # Hit `q` to exit
            break
    
    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()    

def showMovie():
    msBetweenFrames=Entry_fps_movie_value.get()
#    print(msBetweenFrames)
    outputDir = filepathOutputDirTextFrame.get("1.0",'end-1c')
    outputfileName = outputDir + '/' +  Entry_movieName_value.get() + '.mp4'
#    print(outputfileName)
    
    if outputDir == "":
        outputfileName = filedialog.askopenfilename()
    
#    cap = cv2.VideoCapture('C:/Users/bekah/Documents/test/mv/movie_test.mp4')
    cap = cv2.VideoCapture(outputfileName)
    
    if (cap.isOpened()):
        while True:
            ret, frame = cap.read()
            if ret == False: break
        
        #    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            cv2.imshow('frame',frame)
            if cv2.waitKey(int(msBetweenFrames)) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()

# boolean to determine if startFrame is defined after first click in function click_and_select_start_frame
StartFrame = False
StopByEndFrame = False

def click_and_select_start_frame(event, x, y, flags, param):
    # grab references to the global variables
    global StartFrame
    global StopByEndFrame
    if event == cv2.EVENT_LBUTTONDOWN:
#        print("StartFrame: %s" %StartFrame)
#        print("param: %s" %param)
        cam,jaar,maand,dag,uur,minuten,sec,microsec,ext = get_info_from_timeStamp(param)
#        print(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext)
        if StartFrame == False:
           delete_start_frame_data()
           insert_start_frame_data(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext)
           StartFrame = True
           print('start frame: %s' %param)
#           print("in if statement")
        elif StartFrame == True:
           delete_end_frame_data()  
           insert_end_frame_data(cam,jaar,maand,dag,uur,minuten,sec,microsec,ext)
           StartFrame = False
           StopByEndFrame = True
           print('end frame: %s' %param)
#           print('StopByEndFrame: %s' %StopByEndFrame)
#           print("in de elif")
        
        
def get_info_from_timeStamp(file):
    cam,jaar,maand,dag,uur,minuten,sec,microsec = file.split("_")
    microsec = microsec.split(".")[0]
    ext = os.path.splitext(os.path.abspath(file))[1]
    return cam,jaar,maand,dag,uur,minuten,sec,microsec,ext
       
#widgets tab1

lbl_numOfCams = Label(tab1,text="# cam's:")
lbl_numOfCams.grid(row=0,column=0)

Entry_numOfCams_value = StringVar(value=1)
Entry_numOfCams = Entry(tab1,textvariable=Entry_numOfCams_value,width=10)
Entry_numOfCams.grid(row=0,column=1,sticky="W")

lbl_timeBetweenFrames = Label(tab1,text="time between frames in ms:")
lbl_timeBetweenFrames.grid(row=1,column=0)

Entry_timeBetweenFrames_value = StringVar(value=1000)
Entry_timeBetweenFrames = Entry(tab1,textvariable=Entry_timeBetweenFrames_value,width=10)
Entry_timeBetweenFrames.grid(row=1,column=1,sticky="W")

tab1.grid_rowconfigure(2, minsize=10)

btnFilePath = Button(tab1,text="Save location",command=lambda:saveDir(0))
btnFilePath.grid(row=3,column=0)

filepathTextFrame_value=StringVar()
filepathTextFrame = Text(tab1,height=2,width=50)
filepathTextFrame.grid(row=3,column=1,columnspan=2,sticky="W")

tab1.grid_rowconfigure(4, minsize=10)

lbl_rotFlip = Label(tab1,text='Rotate/Flip images:')
lbl_rotFlip.grid(row=5,rowspan=4,column=0)

rotCam1=IntVar()
checkCam1rot = Checkbutton(tab1, text="cam 1: rotate 90",command=lambda:printToFeedbackWindow("Rotate cam1 90°"),variable=rotCam1, onvalue=1,offvalue=0)
checkCam1rot.grid(row=5,column=1,sticky="W")

rotCam2=IntVar()
checkCam2rot = Checkbutton(tab1, text="cam 2: rotate 90",command=lambda:printToFeedbackWindow("Rotate cam2 90°"),variable=rotCam2, onvalue=1,offvalue=0)
checkCam2rot.grid(row=6,column=1,sticky="W")

rotCam3=IntVar()
checkCam3rot = Checkbutton(tab1, text="cam 3: rotate 90",command=lambda:printToFeedbackWindow("Rotate cam3 90°"),variable=rotCam3, onvalue=1,offvalue=0)
checkCam3rot.grid(row=7,column=1,sticky="W")

rotCam4=IntVar()
checkCam4rot = Checkbutton(tab1, text="cam 4: rotate 90",command=lambda:printToFeedbackWindow("Rotate cam4 90°"),variable=rotCam4, onvalue=1,offvalue=0)
checkCam4rot.grid(row=8,column=1,sticky="W")

flipCam1=IntVar()
checkCam1flip = Checkbutton(tab1, text="cam 1: flip",command=lambda:printToFeedbackWindow("Mirror cam1"),variable=flipCam1, onvalue=1,offvalue=0)
checkCam1flip.grid(row=5,column=2,sticky="W")

flipCam2=IntVar()
checkCam2flip = Checkbutton(tab1, text="cam 2: flip",command=lambda:printToFeedbackWindow("Mirror cam2"),variable=flipCam2, onvalue=1,offvalue=0)
checkCam2flip.grid(row=6,column=2,sticky="W")

flipCam3=IntVar()
checkCam3flip = Checkbutton(tab1, text="cam 3: flip",command=lambda:printToFeedbackWindow("Mirror cam3"),variable=flipCam3, onvalue=1,offvalue=0)
checkCam3flip.grid(row=7,column=2,sticky="W")

flipCam4=IntVar()
checkCam4flip = Checkbutton(tab1, text="cam 4: flip",command=lambda:printToFeedbackWindow("Mirror cam4"),variable=flipCam4, onvalue=1,offvalue=0)
checkCam4flip.grid(row=8,column=2,sticky="W")

tab1.grid_rowconfigure(9, minsize=10)

#btnCam1 = Button(window,text="show cam 1",command=lambda:showCam(1))
#btnCam1.grid(row=8,column=0)
#
#btnCam2 = Button(window,text="show cam 2",command=lambda:showCam(2))
#btnCam2.grid(row=8,column=1)
#
#btnCam3 = Button(window,text="show cam 3",command=lambda:showCam(3))
#btnCam3.grid(row=9,column=0)
#
#btnCam4 = Button(window,text="show cam 4",command=lambda:showCam(4))
#btnCam4.grid(row=9,column=1)

#tab1.grid_rowconfigure(10, minsize=10)

lbl_feedbackFrame = Label(tab1,text="Feedback window:")
lbl_feedbackFrame.grid(row=10,column=0)

feedbackTextFrame = Text(tab1,height=1,width=50)
feedbackTextFrame.grid(row=10,column=1,columnspan=2)

#progressbar = ttk.Progressbar(window, mode='indeterminate')
#progressbar.grid(row=12,column=0, columnspan=2)

tab1.grid_rowconfigure(11, minsize=10)

btnExecute = Button(tab1,text="Press to run: CAPTURE PICTURES",command=lambda:start_runProgram_thread(None), fg="green")
btnExecute.grid(row=12,column=1,columnspan=2)

lbl_quit_value = StringVar()
lbl_quit = Label(tab1,text='Press "q" to quit in view',textvariable=lbl_quit_value)
lbl_quit .grid(row=13,column=1,columnspan=2)

#add widgets tab2
tab2.grid_rowconfigure(0, minsize=10)

btnStartPic = Button(tab2,text="Select start picture:",command=lambda:saveDir(1))
btnStartPic.grid(row=1,column=0)

filepathStartFolderTextFrame = Text(tab2,height=2,width=50)
filepathStartFolderTextFrame.grid(row=1,column=1,columnspan=9,sticky="W")

lbl_cam = Label(tab2,text="camera:")
lbl_cam.grid(row=2,column=1,sticky="WE")

lbl_jaar = Label(tab2,text="year:")
lbl_jaar.grid(row=2,column=2,sticky="WE")

lbl_maand = Label(tab2,text="month:")
lbl_maand.grid(row=2,column=3,sticky="WE")

lbl_dag = Label(tab2,text="day:")
lbl_dag.grid(row=2,column=4,sticky="WE")

lbl_uur = Label(tab2,text="hour:")
lbl_uur.grid(row=2,column=5,sticky="WE")

lbl_min = Label(tab2,text="min:")
lbl_min.grid(row=2,column=6,sticky="WE")

lbl_sec = Label(tab2,text="sec:")
lbl_sec.grid(row=2,column=7,sticky="WE")

lbl_msec = Label(tab2,text="msec:")
lbl_msec.grid(row=2,column=8,sticky="WE")

lbl_ext = Label(tab2,text="ext:")
lbl_ext.grid(row=2,column=9,sticky="WE")

lblStartPic = Label(tab2,text="Start picture:")
lblStartPic.grid(row=3,column=0)

camTFStart = Text(tab2,height=2,width=5)
camTFStart.grid(row=3,column=1,sticky="WE")

jaarTFStart = Text(tab2,height=2,width=5)
jaarTFStart.grid(row=3,column=2,sticky="WE")

maandTFStart = Text(tab2,height=2,width=5)
maandTFStart.grid(row=3,column=3,sticky="WE")

dagTFStart = Text(tab2,height=2,width=5)
dagTFStart.grid(row=3,column=4,sticky="WE")

uurTFStart = Text(tab2,height=2,width=5)
uurTFStart.grid(row=3,column=5,sticky="WE")

minTFStart = Text(tab2,height=2,width=5)
minTFStart.grid(row=3,column=6,sticky="WE")

secTFStart = Text(tab2,height=2,width=5)
secTFStart.grid(row=3,column=7,sticky="WE")

msecTFStart = Text(tab2,height=2,width=5)
msecTFStart.grid(row=3,column=8,sticky="WE")

extTFStart = Text(tab2,height=2,width=5)
extTFStart.grid(row=3,column=9,sticky="WE")

#tab2.grid_rowconfigure(4, minsize=10)

btnShowPictures = Button(tab2,text="dry run",command=lambda:dryRun(), fg="orange")
btnShowPictures.grid(row=4,column=0)

lblEndPic = Label(tab2,text="End picture:")
lblEndPic.grid(row=5,column=0)


camTFEnd = Text(tab2,height=2,width=5)
camTFEnd.grid(row=5,column=1,sticky="WE")

jaarTFEnd = Text(tab2,height=2,width=5)
jaarTFEnd.grid(row=5,column=2,sticky="WE")

maandTFEnd = Text(tab2,height=2,width=5)
maandTFEnd.grid(row=5,column=3,sticky="WE")

dagTFEnd = Text(tab2,height=2,width=5)
dagTFEnd.grid(row=5,column=4,sticky="WE")

uurTFEnd = Text(tab2,height=2,width=5)
uurTFEnd.grid(row=5,column=5,sticky="WE")

minTFEnd = Text(tab2,height=2,width=5)
minTFEnd.grid(row=5,column=6,sticky="WE")

secTFEnd = Text(tab2,height=2,width=5)
secTFEnd.grid(row=5,column=7,sticky="WE")

msecTFEnd = Text(tab2,height=2,width=5)
msecTFEnd.grid(row=5,column=8,sticky="WE")

extTFEnd = Text(tab2,height=2,width=5)
extTFEnd.grid(row=5,column=9,sticky="WE")

tab2.grid_rowconfigure(6, minsize=10)

btnOutputDir = Button(tab2,text="Output directory:",command=lambda:saveDir(3))
btnOutputDir.grid(row=7,column=0)

filepathOutputDir_value=StringVar()
filepathOutputDirTextFrame = Text(tab2,height=2,width=50)
filepathOutputDirTextFrame.grid(row=7,column=1,columnspan=9,sticky="W")

tab2.grid_rowconfigure(8, minsize=10)

lbl_movieName = Label(tab2,text="name movie:")
lbl_movieName.grid(row=9,column=0)

Entry_movieName_value = StringVar(value="movie")
Entry_movieName = Entry(tab2,textvariable=Entry_movieName_value)
Entry_movieName.grid(row=9,column=1,columnspan=3,sticky="W")

lbl_movieNameExtension = Label(tab2,text=".mp4")
lbl_movieNameExtension.grid(row=9,column=4)

lbl_fps = Label(tab2,text="Frames per second (fps):")
lbl_fps.grid(row=10,column=0)

Entry_fps_value = StringVar(value=10)
Entry_fps = Entry(tab2,textvariable=Entry_fps_value)
Entry_fps.grid(row=10,column=1,columnspan=3,sticky="W")

#feedbackTextFrame = Text(tab2,height=2,width=45)
#feedbackTextFrame.grid(row=11,column=1,columnspan=9,sticky="W")

tab2.grid_rowconfigure(11, minsize=10)

btnExecute = Button(tab2,text="RUN: Make movie from pictures",command=lambda:makeMovieFromPictures(), fg="green")
btnExecute.grid(row=12,column=1,columnspan=4,sticky="W")

btnShowMovie = Button(tab2,text="Show movie",command=lambda:showMovie(), fg="red")
btnShowMovie.grid(row=12,column=5,columnspan=2,sticky="E")

Entry_fps_movie_value = StringVar(value=25)
Entry_fps_movie = Entry(tab2,textvariable=Entry_fps_movie_value,width=5)
Entry_fps_movie.grid(row=12,column=7)

lbl_msBetweenFrames = Label(tab2,text="ms <> frames")
lbl_msBetweenFrames.grid(row=12,column=8,columnspan=2,sticky="W")

root.mainloop()
    