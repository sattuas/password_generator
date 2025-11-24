from tkinter import *
from tkinter.ttk import *
from models.generator import PasswordGenerator
import webbrowser


def get_password():
    first_password()
    
    try:
        pw = PasswordGenerator(16,
                            uppercase_letters.get(),
                            lowercase_letters.get(),
                            symbols.get(),
                            digits.get())

        message.set(pw.generate())
    except IndexError as e:
        print(f'Error! {e}')


def copy_clipboard():
    root.clipboard_clear()
    root.clipboard_append(message.get())
    root.update()
    flash.set("copied to clipboard!")
    root.after(600, lambda: flash.set(""))


def first_password():
    global firstpw  
    if firstpw == False:
        copy.configure(state="normal")
        firstpw = True


def open_link(event):
    webbrowser.open("https://github.com/")


firstpw = False

root = Tk()
root.title("Password Generator")
root.geometry("500x320")

img = PhotoImage(file="assets/images/chibi_coding2.png")
# img = img.subsample(5, 5)

result = Frame(root)

uppercase_letters = IntVar()
lowercase_letters = IntVar()
symbols = IntVar()
digits = IntVar()

flash = StringVar()
message = StringVar()
message.set("Password will be show here")

title = Label(root,
              text="GENERATE A PASSWORD",
              font=("Arial", 16, "bold"))

button = Button(root,
                text="Generate",
                command=get_password)

show_password = Label(result,
                      textvariable=message)

copy = Button(result,
              text="Copy",
              command=copy_clipboard,
              state="disabled")

flash_lbl = Label(root,
                  textvariable=flash)

checkbuttons_frame = Frame(root)

Upper = Checkbutton(checkbuttons_frame,
                    text="Upper A-Z",
                    variable=uppercase_letters,
                    onvalue=1,
                    offvalue=0)

Lower = Checkbutton(checkbuttons_frame,
                    text="Lower a-z",
                    variable=lowercase_letters,
                    onvalue=1,
                    offvalue=0)

Symbols = Checkbutton(checkbuttons_frame,
                      text="Symbols @#!..",
                      variable=symbols,
                      onvalue=1,
                      offvalue=0)

Digits = Checkbutton(checkbuttons_frame,
                     text="Digits 0-9",
                     variable=digits,
                     onvalue=1,
                     offvalue=0)

image_lbl = Label(root, image=img)

credit = Label(root, text="Made by")
credit_link = Label(root, text="Sattua :)", foreground="blue", cursor="hand2")

title.pack(pady=15)

checkbuttons_frame.pack(pady=(0, 20))
Upper.pack(side="left", padx=10)
Lower.pack(side="left", padx=10)
Symbols.pack(side="left", padx=10)
Digits.pack(side="left", padx=10)

button.pack(pady=(0, 20))
result.pack()
show_password.pack(side="left")
copy.pack(side="right")
flash_lbl.pack()

image_lbl.pack()

credit.pack()
credit_link.pack()

credit_link.bind("<Button-1>", open_link)

root.resizable(False, False)

root.mainloop()
