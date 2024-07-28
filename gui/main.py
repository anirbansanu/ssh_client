import tkinter as tk
from tkinter import ttk
from gui.sftp_gui import SFTPWindow
from gui.ssh_gui import SSHWindow

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SSH Client")
        self.geometry("400x200")

        self.sftp_button = ttk.Button(self, text="SFTP Client", command=self.open_sftp_window)
        self.sftp_button.pack(pady=10)

        self.ssh_button = ttk.Button(self, text="SSH Client", command=self.open_ssh_window)
        self.ssh_button.pack(pady=10)

    def open_sftp_window(self):
        SFTPWindow(self)

    def open_ssh_window(self):
        SSHWindow(self)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
