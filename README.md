# multiple-webcam-capturing
Add up to 4 webcams to your laptop.

Please feel free to contribute or use as is. I believe there is a lot of improvement possible and extra features which can be added.

You can make an executable through Pyinstaller (converting a python script to a standalone programma)
  1. open the command prompt
  2. go to the directory where your programma (.py) file lives
  3. type: pyinstaller.exe  --windowed yourprogramme.py
    - If Pyinstaller is not in your environment variable you have to write down the full path to pyinstaller.exe
    - the flag windowed is necessary for GUI applications
    - extra options:
      --icon = yourIcon.ico
      --onefile make a "one file" executabel
  4. after creation you get a
    - "build" dir which is a tempory dir (you can delete this one)
    - "dist" dir which contains the .exe file and all the files needed to run the programma
   

regards,

Karim
