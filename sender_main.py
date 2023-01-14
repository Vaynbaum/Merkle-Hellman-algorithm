from tkinter import *

from common.const import *
from common.work_file import *
from sender import Sender


def encrypt_message():
    key = read_json_file(DIR_KEY)
    text = editor.get("1.0", "end")
    enc_txt = sender.Encrypt(text[: len(text) - 1], key)
    write_file(DIR_ENC_TXT, enc_txt)


root = Tk()
root.title("Sender")
root.geometry("300x250")
sender = Sender()

Button(root, text="Encrypt the message", command=encrypt_message).pack(side=BOTTOM, pady=5)
editor = Text(root)
editor.pack(anchor=N, fill=X, pady=5)
