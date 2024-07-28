import tkinter as tk
from tkinter import ttk, messagebox
from core.ssh_client import SSHClient

class SSHWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("SSH Client")
        self.geometry("400x300")

        self.hostname_label = ttk.Label(self, text="Hostname:")
        self.hostname_label.pack(pady=5)
        self.hostname_entry = ttk.Entry(self)
        self.hostname_entry.pack(pady=5)

        self.port_label = ttk.Label(self, text="Port:")
        self.port_label.pack(pady=5)
        self.port_entry = ttk.Entry(self)
        self.port_entry.pack(pady=5)

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.connect_button = ttk.Button(self, text="Connect", command=self.connect_to_ssh)
        self.connect_button.pack(pady=10)

    def connect_to_ssh(self):
        hostname = self.hostname_entry.get()
        port = int(self.port_entry.get())
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            self.ssh_client = SSHClient(hostname, port, username, password)
            self.ssh_client.connect()
            messagebox.showinfo("Success", "Connected to SSH server")
        except Exception as e:
            messagebox.showerror("Error", str(e))
