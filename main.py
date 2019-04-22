# coding=utf-8

import time
import pyperclip

from threading import Thread
from translate_api import translate

from Tkinter import *

RUNNING = True


class TranslationWindow(object, Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.wm_attributes('-topmost', 1)
        self.master.title('translation')
        self.pack()
        self.content = Text(self, height=3, width=30, bg='#FFF0F5')
        self.content.pack()
        self.button_run = Button(self, text='run', width=5, height=1, command=self._run)
        self.button_run.pack(side='left')
        self.button_stop = Button(self, text='stop', width=5, height=1, command=self._stop)
        self.button_stop.pack(side='left')

    def _run(self):
        global RUNNING
        RUNNING = True
        Scanner(self).start()
        self.set_content('running')

    @staticmethod
    def _stop():
        global RUNNING
        RUNNING = False

    def quit(self):
        self._stop()
        super(TranslationWindow, self).quit()

    def set_content(self, text):
        self.content.delete(0.0, END)
        self.content.insert(END, text)


class Scanner(Thread):
    def __init__(self, window):
        super(Scanner, self).__init__()
        self.window = window

    def run(self):
        global RUNNING
        last_paste = pyperclip.paste()
        while True:
            if not RUNNING:
                self.window.set_content('stopped')
                break
            now_paste = pyperclip.paste()
            if now_paste != last_paste:
                try:
                    self.window.set_content(translate(now_paste))
                except Exception as ex:
                    print('translate [%s] failed, msg is [%s]' % (now_paste, ex.message))
                last_paste = now_paste
            time.sleep(0.5)


if __name__ == '__main__':
    translation_window = TranslationWindow()
    translation_window.mainloop()
