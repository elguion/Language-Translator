from tkinter import Tk, Text, Button, Frame, Label
from tkinter.ttk import Combobox
from textblob import TextBlob
from googletrans import Translator

# Translator function
def translate_text():
    text = text_input.get(1.0, "end-1c")
    blob = TextBlob(text)
    source_lang = blob.detect_language()
    translator = Translator()

    if source_lang != 'en':
        translated = translator.translate(text, src=source_lang, dest='en')
        result = translator.translate(translated.text, dest=selected_language.get())
    else:
        result = translator.translate(text, dest=selected_language.get())

    text_output.delete(1.0, "end")
    text_output.insert("end", result.text)


# Tkinter GUI
root = Tk()
root.title("Language Translator")
root.geometry("400x300")
root.configure(bg='black')
root.option_add('*Font', 'Roboto')

top_frame = Frame(root, bg='black')
top_frame.pack(pady=20)

text_input = Text(top_frame, wrap="word", height=6, width=40, bg='white', fg='black')
text_input.pack()

middle_frame = Frame(root, bg='black')
middle_frame.pack(pady=10)

button = Button(middle_frame, text="Translate", command=translate_text, bg='red', fg='white')
button.pack(side='left', padx=10)

languages = ["fr", "de"]
selected_language = Combobox(middle_frame, values=languages)
selected_language.set("fr")  # default language is French
selected_language.pack(side='left')

bottom_frame = Frame(root, bg='black')
bottom_frame.pack(pady=20)

text_output = Text(bottom_frame, wrap="word", height=6, width=40, bg='white', fg='black')
text_output.pack()

root.mainloop()
