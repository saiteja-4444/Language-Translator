import imp
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Translator_py')
root.geometry("900x300")

# Set the default font for all widgets to Salsa
root.option_add("*Font", "Salsa")

def translate_it():
    translated_text.delete(1.0, END)
    try:

        for key, value in languages.items():
            if(value == original_combo.get()):
                from_language_key = key
        for key, value in languages.items():
            if(value == translated_combo.get()):
                to_language_key = key
        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(
            from_lang=from_language_key, to=to_language_key)
        translated_text.insert(1.0, words)
    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=15, padx=20)

# Set button colors to blue
translate_button = Button(root, text="TRANSLATE", font=("Salsa", 24), bg="blue", fg="white", command=translate_it)
translate_button.grid(row=0, column=1, padx=10)
translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# Clear button with blue color
clear_button = Button(root, text="Clear", bg="blue", fg="white", command=clear)
clear_button.grid(row=2, column=1)

# combo boxes
original_combo = ttk.Combobox(root, width=40, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=40, value=language_list)
translated_combo.current(38)
translated_combo.grid(row=1, column=2)

root.mainloop()
