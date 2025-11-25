import tkinter as tk
from tkinter import ttk
from .generator import PasswordGenerator
import webbrowser


class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x320")
        self.root.resizable(False, False)

        self.first_password_generated = False

        self.uppercase = tk.IntVar(value=1)
        self.lowercase = tk.IntVar(value=1)
        self.symbols = tk.IntVar(value=1)
        self.digits = tk.IntVar(value=1)

        self.flash = tk.StringVar()
        self.message = tk.StringVar(value="Password will be shown here")

        self.build_ui()

    def build_ui(self):
        img = tk.PhotoImage(file="./assets/images/chibi_coding2.png")
        self.image_lbl = ttk.Label(self.root, image=img)
        self.image_lbl.image = img

        title = ttk.Label(self.root, text="GENERATE A PASSWORD", font=("Arial", 16, "bold"))
        title.pack(pady=15)

        cb_frame = ttk.Frame(self.root)
        cb_frame.pack(pady=(0, 20))

        ttk.Checkbutton(cb_frame, text="Upper A-Z", variable=self.uppercase).pack(side="left", padx=10)
        ttk.Checkbutton(cb_frame, text="Lower a-z", variable=self.lowercase).pack(side="left", padx=10)
        ttk.Checkbutton(cb_frame, text="Symbols @#!...", variable=self.symbols).pack(side="left", padx=10)
        ttk.Checkbutton(cb_frame, text="Digits 0-9", variable=self.digits).pack(side="left", padx=10)

        ttk.Button(self.root, text="Generate", command=self.get_password).pack(pady=(0, 20))

        result = ttk.Frame(self.root)
        result.pack()

        ttk.Label(result, textvariable=self.message).pack(side="left")

        self.copy_btn = ttk.Button(result, text="Copy", command=self.copy_clipboard, state="disabled")
        self.copy_btn.pack(side="right")

        ttk.Label(self.root, textvariable=self.flash).pack()
        
        self.image_lbl.pack()

        ttk.Label(self.root, text="Made by").pack()

        self.credit_link = ttk.Label(self.root, text="Sattua :)", foreground="blue", cursor="hand2")
        self.credit_link.pack()

        self.credit_link.bind("<Button-1>", self.open_link)
    

    def get_password(self):
        try:
            gen = PasswordGenerator(
                16,
                self.uppercase.get(),
                self.lowercase.get(),
                self.symbols.get(),
                self.digits.get()
            )
            self.message.set(gen.generate())
            
            if not self.first_password_generated:
                self.copy_btn.configure(state="normal")
                self.first_password_generated = True

        except IndexError as e:
            print(f'Error generating password: {e}')

    def copy_clipboard(self):
        pw = self.message.get()
        
        self.root.clipboard_clear()
        self.root.clipboard_append(pw)
        self.root.update()

        self.flash.set("Copied to Clipboard!")
        self.root.after(600, lambda: self.flash.set(""))

    def open_link(self, event):
        webbrowser.open("https://github.com/sattuas")

        
if __name__ == "__main__":
    root = tk.Tk()
    PasswordApp(root)
    root.mainloop()