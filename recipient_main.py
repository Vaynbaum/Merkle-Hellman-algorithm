from tkinter import *

from recipient import Recipient
from common.const import *
from common.work_file import *


def create_keys():
    key = recipient.CreateKeys()
    write_json_file(DIR_KEY, key)


def get_message():
    text = read_full_file(DIR_ENC_TXT)
    set_text(text)


def decrypt_message():
    text = entry.get("1.0", "end")
    dec_text = recipient.Decrypt(text[: len(text) - 1])
    set_text(dec_text)


def set_text(text):
    entry.delete("1.0", END)
    entry.insert("1.0", text)


recipient = Recipient()
root = Tk()
root.title("Recipient")
root.geometry("300x250")

Button(root, text="Generate keys", command=create_keys, width=40).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
Button(root, text="Get a message", command=get_message).grid(row=2, column=0)
Button(root, text="Decrypt the message", command=decrypt_message).grid(row=2, column=1)
entry = Text(root, width=35, height=10)
entry.grid(row=1, column=0, columnspan=2, pady=5)


