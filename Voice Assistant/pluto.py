# # import pyttsx3
# # import urllib.parse
# # import speech_recognition as sr
# # from datetime import date
# # import time
# # import webbrowser
# # import datetime
# # import subprocess
# # from pynput.keyboard import Key, Controller
# # import pyautogui
# # import sys
# # import os
# # from os import listdir
# # from os.path import isfile, join
# # import smtplib
# # import wikipedia
# # import Gesture_Controller
# # import app
# # from threading import Thread

# # # -------------Object Initialization---------------
# # today = date.today()
# # r = sr.Recognizer()
# # keyboard = Controller()
# # engine = pyttsx3.init('sapi5')  # Initialize TTS engine only once
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[0].id)

# # # Set Chrome path
# # chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"

# # # ----------------Variables------------------------
# # file_exp_status = False
# # files = []
# # path = ''
# # is_awake = True  # Bot status

# # # ------------------Functions----------------------
# # def reply(audio):
# #     app.ChatBot.addAppMsg(audio)
# #     print(audio)
# #     engine.say(audio)
# #     engine.runAndWait()

# # def wish():
# #     hour = int(datetime.datetime.now().hour)
# #     if hour >= 0 and hour < 12:
# #         reply("Good Morning!")
# #     elif hour >= 12 and hour < 18:
# #         reply("Good Afternoon!")   
# #     else:
# #         reply("Good Evening!")  
# #     reply("I am Astra, How can I help you?")

# # def record_audio():
# #     with sr.Microphone() as source:
# #         r.pause_threshold = 0.6  # Reduce pause threshold
# #         r.energy_threshold = 350  # Adjust sensitivity to reduce delay
# #         voice_data = ''
# #         try:
# #             # Increase the phrase_time_limit to 5 seconds to capture longer commands
# #             audio = r.listen(source, phrase_time_limit=5)
# #             voice_data = r.recognize_google(audio)
# #         except sr.RequestError as e:
# #             reply('Sorry, my service is down. Check your Internet connection')
# #         except sr.UnknownValueError:
# #             pass
# #         return voice_data.lower()


# # # Define command actions
# # def open_google():
# #     reply("What do you want to search for?")
# #     search_query = record_audio()
    
# #     # Check the recorded audio
# #     print(f"Recorded Search Query: {search_query}")
    
# #     app.eel.addUserMsg(search_query)
# #     reply(f'Searching for {search_query} on Google.')
    
# #     # URL encode the search query
# #     url = 'https://google.com/search?q=' + urllib.parse.quote(search_query)
    
# #     # Open the URL using subprocess to launch Chrome
# #     try:
# #         subprocess.Popen([chrome_path, url])
# #         reply('This is what I found!')
# #     except Exception as e:
# #         reply("Failed to open Chrome.")
# #         print(f"Error: {e}")

# # def search_google(query):
# #     reply('Searching for ' + query)
    
# #     # URL encode the search query
# #     url = 'https://google.com/search?q=' + urllib.parse.quote(query)
# #     subprocess.Popen([chrome_path, url])
# #     reply('This is what I found, Sir.')
    
# # def close_application(application_name):
# #     # Function to close a specific application
# #     reply(f"Closing {application_name}...")
# #     os.system(f'taskkill /im {application_name} /f')
    
# # def open_calendar():
# #     reply("Opening the calendar...")
# #     subprocess.Popen(['explorer.exe', 'shell:calendar'])

# # def open_calculator():
# #     reply("Opening the calculator...")
# #     subprocess.Popen(['calc.exe'])

# # def open_camera():
# #     reply("Opening the camera...")
# #     try:
# #         import cv2
# #         cap = cv2.VideoCapture(0)
# #         while cap.isOpened():
# #             ret, frame = cap.read()
# #             if not ret:
# #                 reply("Failed to grab frame")
# #                 break
# #             cv2.imshow('Camera', frame)
# #             if cv2.waitKey(1) & 0xFF == ord('q'):
# #                 break
# #         cap.release()
# #         cv2.destroyAllWindows()
# #         reply("Camera closed.")
# #     except Exception as e:
# #         reply('Failed to open the camera.')
# #         print(f"Error opening camera: {e}")
# # def open_word():
# #     reply("Opening Microsoft Word...")
# #     subprocess.Popen(['C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE'])

# # def open_excel():
# #     reply("Opening Microsoft Excel...")
# #     subprocess.Popen(['C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE'])

# # def open_powerpoint():
# #     reply("Opening Microsoft PowerPoint...")
# #     subprocess.Popen(['C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE'])
    
# # def open_notepad():
# #     reply("Opening Notepad...")
# #     subprocess.Popen(['notepad.exe'])

# # # Command dictionary
# # commands = {
# #     'open google': open_google,
# #     'search': search_google,
# #     'close google': lambda: close_application("chrome.exe"),
# #     'open calendar': open_calendar,
# #     'open calculator': open_calculator,
# #     'open camera': open_camera,
# #     'open word': open_word,
# #     'open excel': open_excel,
# #     'open powerpoint': open_powerpoint,
# #     'open notepad': open_notepad
# # }

# # # ------------------Driver Code--------------------

# # t1 = Thread(target=app.ChatBot.start)
# # t1.start()

# # # Lock main thread until Chatbot has started
# # while not app.ChatBot.started:
# #     time.sleep(0.5)

# # wish()
# # voice_data = None
# # while True:
# #     if app.ChatBot.isUserInput():
# #         voice_data = app.ChatBot.popUserInput()
# #     else:
# #         voice_data = record_audio()

# #     # process voice_data
# #     if voice_data and 'astra' in voice_data:
# #         try:
# #             voice_data = voice_data.replace('astra', '').strip()  # Clean voice data
# #             for command in commands:
# #                 if command in voice_data:
# #                     if command == 'open folder':
# #                         # Get the folder name from the voice command
# #                         folder_name = voice_data.split('open folder ')[-1].strip()
# #                         commands[command](folder_name)  # Call with folder name
# #                     else:
# #                         commands[command]()  # Call the function directly
# #                     break
# #         except SystemExit:
# #             reply("Exit Successful")
# #             break
# #         except Exception as e:
# #             print(f"EXCEPTION: {e}")  # Catch other exceptions for debugging
# #             break

import pyttsx3
import urllib.parse
import speech_recognition as sr
from datetime import date
import time
import webbrowser
import datetime
import subprocess
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
import Gesture_Controller
import cv2
import app
from threading import Thread


# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()
keyboard = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set Chrome path
chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"

# ----------------Variables------------------------
file_exp_status = False
files = []
path = ''
is_awake = True  # Bot status

# ------------------Functions----------------------
def reply(audio):
    app.ChatBot.addAppMsg(audio)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        reply("Good Morning!")
    elif hour >= 12 and hour < 18:
        reply("Good Afternoon!")   
    else:
        reply("Good Evening!")  
    reply("I am Pluto,How can I help you?")

# Set Microphone parameters
with sr.Microphone() as source:
    r.energy_threshold = 500 
    r.dynamic_energy_threshold = False

# Audio to String
def record_audio():
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)
        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry, My Service is down. Please check your Internet connection')
        except sr.UnknownValueError:
            pass
        return voice_data.lower()

# Function to open Google with a search query
def open_google():
    reply("What do you want to search for?")
    search_query = record_audio()
    print(f"Recorded Search Query: {search_query}")
    reply(f'Searching for {search_query} on Google.')
    url = 'https://google.com/search?q=' + urllib.parse.quote(search_query)
    try:
        subprocess.Popen([chrome_path, url])
        reply('This is what I found!')
    except Exception as e:
        reply("Failed to open Chrome.")
        print(f"Error: {e}")

# Executes Commands (input: string)
# def respond(voice_data):
#     global file_exp_status, files, is_awake, path
#     print(voice_data)
#     voice_data.replace('pluto', '')
#     app.eel.addUserMsg(voice_data)

#     if not is_awake:
#         if 'wake up' in voice_data:
#             is_awake = True
#             wish()

#     # STATIC CONTROLS
#     elif 'hello' in voice_data:
#         wish()

#     elif 'what is your name' in voice_data:
#         reply('My name is Pluto!')

#     elif 'date' in voice_data:
#         reply(today.strftime("%B %d, %Y"))

#     elif 'time' in voice_data:
#         reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

#     elif 'search' in voice_data:
#         reply('Searching for ' + voice_data.split('search')[1])
#         url = 'https://google.com/search?q=' + voice_data.split('search')[1]
#         try:
#             webbrowser.get().open(url)
#             reply('This is what I found.')
#         except:
#             reply('Please check your Internet connection.')

#     elif 'location' in voice_data:
#         reply('Which place are you looking for?')
#         temp_audio = record_audio()
#         app.eel.addUserMsg(temp_audio)
#         reply('Locating...')
#         url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
#         try:
#             webbrowser.get().open(url)
#             reply('This is what I found.')
#         except:
#             reply('Please check your Internet connection.')

#     elif ('bye' in voice_data) or ('by' in voice_data):
#         reply("Goodbye! Have a nice day.")
#         is_awake = False

#     elif ('exit' in voice_data) or ('terminate' in voice_data):
#         if Gesture_Controller.GestureController.gc_mode:
#             Gesture_Controller.GestureController.gc_mode = 0
#         app.ChatBot.close()
#         sys.exit()

#     # DYNAMIC CONTROLS
#     elif 'launch gesture recognition' in voice_data:
#         if Gesture_Controller.GestureController.gc_mode:
#             reply('Gesture recognition is already active.')
#         else:
#             gc = Gesture_Controller.GestureController()
#             t = Thread(target=gc.start)
#             t.start()
#             reply('Launched successfully.')

#     elif 'stop gesture recognition' in voice_data:
#         if Gesture_Controller.GestureController.gc_mode:
#             Gesture_Controller.GestureController.gc_mode = 0
#             reply('Gesture recognition stopped.')
#         else:
#             reply('Gesture recognition is already inactive.')

#     elif 'copy' in voice_data:
#         with keyboard.pressed(Key.ctrl):
#             keyboard.press('c')
#             keyboard.release('c')
#         reply('Copied.')

#     elif 'paste' in voice_data:
#         with keyboard.pressed(Key.ctrl):
#             keyboard.press('v')
#             keyboard.release('v')
#         reply('Pasted.')

#     # File Navigation (Default Folder set to C://)
#     elif 'list' in voice_data:
#         counter = 0
#         path = 'C://'
#         files = listdir(path)
#         filestr = ""
#         for f in files:
#             counter += 1
#             print(str(counter) + ':  ' + f)
#             filestr += str(counter) + ':  ' + f + '<br>'
#         file_exp_status = True
#         reply('These are the files in your root directory.')
#         app.ChatBot.addAppMsg(filestr)

#     elif file_exp_status:
#         counter = 0
#         if 'open' in voice_data:
#             if isfile(join(path, files[int(voice_data.split(' ')[-1]) - 1])):
#                 os.startfile(path + files[int(voice_data.split(' ')[-1]) - 1])
#                 file_exp_status = False
#             else:
#                 try:
#                     path = path + files[int(voice_data.split(' ')[-1]) - 1] + '//'
#                     files = listdir(path)
#                     filestr = ""
#                     for f in files:
#                         counter += 1
#                         filestr += str(counter) + ':  ' + f + '<br>'
#                         print(str(counter) + ':  ' + f)
#                     reply('Opened successfully.')
#                     app.ChatBot.addAppMsg(filestr)
#                 except:
#                     reply('You do not have permission to access this folder.')

#         if 'back' in voice_data:
#             filestr = ""
#             if path == 'C://':
#                 reply('Sorry, this is the root directory.')
#             else:
#                 a = path.split('//')[:-2]
#                 path = '//'.join(a) + '//'
#                 files = listdir(path)
#                 for f in files:
#                     counter += 1
#                     filestr += str(counter) + ':  ' + f + '<br>'
#                     print(str(counter) + ':  ' + f)
#                 reply('Ok.')
#                 app.ChatBot.addAppMsg(filestr)

#     else:
#         reply('I am not functioned to do this!')
word_path = r"C:\Program Files\Microsoft Office\Office16\WINWORD.EXE"
excel_path = r"C:\Program Files\Microsoft Office\Office16\EXCEL.EXE"
powerpoint_path = r"C:\Program Files\Microsoft Office\Office16\POWERPNT.EXE"
notepad_path = r"C:\Windows\notepad.exe"

def respond(voice_data):
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('pluto', '')
    app.eel.addUserMsg(voice_data)

    if not is_awake:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    # STATIC CONTROLS
    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        reply('My name is Pluto!')

    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

    elif 'search' in voice_data:
        reply('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' + voice_data.split('search')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found.')
        except:
            reply('Please check your Internet connection.')

    elif 'location' in voice_data:
        reply('Which place are you looking for?')
        temp_audio = record_audio()
        app.eel.addUserMsg(temp_audio)
        reply('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found.')
        except:
            reply('Please check your Internet connection.')

    elif ('bye' in voice_data) or ('by' in voice_data):
        reply("Goodbye! Have a nice day.")
        is_awake = False

    elif ('exit' in voice_data) or ('terminate' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
        app.ChatBot.close()
        sys.exit()

    # DYNAMIC CONTROLS
    elif 'launch gesture recognition' in voice_data:
        if Gesture_Controller.GestureController.gc_mode:
            reply('Gesture recognition is already active.')
        else:
            gc = Gesture_Controller.GestureController()
            t = Thread(target=gc.start)
            t.start()
            reply('Launched successfully.')

    elif 'stop gesture recognition' in voice_data:
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
            reply('Gesture recognition stopped.')
        else:
            reply('Gesture recognition is already inactive.')

    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        reply('Copied.')

    elif 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        reply('Pasted.')

    # New functionality to open applications
    elif 'open word' in voice_data:
        subprocess.Popen([word_path])
        reply("Opening Microsoft Word.")

    elif 'open excel' in voice_data:
        subprocess.Popen([excel_path])
        reply("Opening Microsoft Excel.")

    elif 'open powerpoint' in voice_data:
        subprocess.Popen([powerpoint_path])
        reply("Opening Microsoft PowerPoint.")

    elif 'open notepad' in voice_data:
        subprocess.Popen([notepad_path])
        reply("Opening Notepad.")

    # File Navigation (Default Folder set to C://)
    elif 'list' in voice_data:
        counter = 0
        path = 'C://'
        files = listdir(path)
        filestr = ""
        for f in files:
            counter += 1
            print(str(counter) + ':  ' + f)
            filestr += str(counter) + ':  ' + f + '<br>'
        file_exp_status = True
        reply('These are the files in your root directory.')
        app.ChatBot.addAppMsg(filestr)

    elif file_exp_status:
        counter = 0
        if 'open' in voice_data:
            if isfile(join(path, files[int(voice_data.split(' ')[-1]) - 1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1]) - 1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1]) - 1] + '//'
                    files = listdir(path)
                    filestr = ""
                    for f in files:
                        counter += 1
                        filestr += str(counter) + ':  ' + f + '<br>'
                        print(str(counter) + ':  ' + f)
                    reply('Opened successfully.')
                    app.ChatBot.addAppMsg(filestr)
                except:
                    reply('You do not have permission to access this folder.')

        if 'back' in voice_data:
            filestr = ""
            if path == 'C://':
                reply('Sorry, this is the root directory.')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a) + '//'
                files = listdir(path)
                for f in files:
                    counter += 1
                    filestr += str(counter) + ':  ' + f + '<br>'
                    print(str(counter) + ':  ' + f)
                reply('Ok.')
                app.ChatBot.addAppMsg(filestr)

    else:
        reply('I am not functioned to do this!')

# ------------------Driver Code--------------------
t1 = Thread(target=app.ChatBot.start)
t1.start()

# Lock main thread until Chatbot has started
while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:
    if app.ChatBot.isUserInput():
        voice_data = app.ChatBot.popUserInput()
    else:
        voice_data = record_audio()

    # Process voice_data
    if 'pluto' in voice_data:
        try:
            respond(voice_data)
        except SystemExit:
            reply("Exit successful.")
            break
        except Exception as e:
            print(f"EXCEPTION raised while closing: {e}")
            break
