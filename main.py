import tkinter as tk
from datetime import datetime

class App:

    def __init__(self, root):
        self.root = root
        root.title("Label text change sample")
        root.geometry("250x100")

        self.datetime_label = tk.Label(root, text="")
        self.datetime_label.pack()

        tk.Button(text="Display datetime", width=20, command=self.display_datetime).pack()
        root.mainloop()

    def display_datetime(self):
        self.datetime_label["text"] = datetime.now()


def main():
    root = tk.Tk()
    app = App(root)
    app.root.mainloop()


if __name__ == "__main__":
    main()
