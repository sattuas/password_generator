import tkinter as tk
from tkinter import ttk
from generator import PasswordGenerator


class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x320")
        self.root.resizable(False, False)

        self.first_password_generated = False

        self.uppercase = tk.IntVar()
        self.lowercase = tk.IntVar()
        self.symbols = tk.IntVar()
        self.digits = tk.IntVar()

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
    

    def get_password(self):
        ...

    def copy_clipboard(self):
        ...

        
if __name__ == "__main__":
    root = tk.Tk()
    PasswordApp(root)
    root.mainloop()