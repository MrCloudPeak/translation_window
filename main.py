# coding=utf-8

import time
import pyperclip

from threading import Thread
from translate_api import translate

from Tkinter import *


class TranslationWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.wm_attributes('-topmost', 1)
        self.master.title('translation')
        self.pack()
        self.content = Text(self, height=3, width=30, bg='#FFF0F5')
        self.content.pack()

    def set_content(self, text):
        self.content.delete(0.0, END)
        self.content.insert(END, text)


class Scanner(Thread):
    def __init__(self, window):
        super(Scanner, self).__init__()
        self.window = window

    def run(self):
        last_paste = pyperclip.paste()
        while True:
            now_paste = pyperclip.paste()
            if now_paste != last_paste:
                self.window.set_content(translate(now_paste))
                last_paste = now_paste
            time.sleep(0.5)


if __name__ == '__main__':
    translation_window = TranslationWindow()
    Scanner(translation_window).start()
    translation_window.mainloop()
