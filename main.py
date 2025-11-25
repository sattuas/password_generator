import tkinter as tk
from models.app import PasswordApp


if __name__ == "__main__":
    root = tk.Tk()
    PasswordApp(root)
    root.mainloop()