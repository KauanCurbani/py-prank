from pynput.mouse import Listener
import webbrowser
import subprocess
from playsound import playsound


click_count = 0
shown = 0


def audio_manager():
    subprocess.run(["amixer",
                    "-D",
                    "pulse" ,
                    "sset" ,
                    "Master",
                    "unmute",])
    subprocess.run(["amixer",
                    "-D",
                    "pulse" ,
                    "sset" ,
                    "Master",
                    "100%+",])
        


def on_click(x, y, button, pressed):
    global click_count
    global shown

    
    if pressed:
        click_count += 1
    if click_count > 10:
        shown += 1
        audio_manager()
        if (shown % 2 == 1):
            webbrowser.open('https://bembomsalgados.com.br/')
        else:
            webbrowser.open('http://www.maissaborsalgados.com.br/')
        playsound('audio.mp3')
        click_count = 0

with Listener(on_click=on_click) as listener:
    listener.join();