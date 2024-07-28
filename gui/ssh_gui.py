from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.ssh_client import SSHClient

class SSHWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SSH Client")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.hostname_label = QLabel("Hostname:")
        layout.addWidget(self.hostname_label)
        self.hostname_entry = QLineEdit()
        layout.addWidget(self.hostname_entry)

        self.port_label = QLabel("Port:")
        layout.addWidget(self.port_label)
        self.port_entry = QLineEdit()
        layout.addWidget(self.port_entry)

        self.username_label = QLabel("Username:")
        layout.addWidget(self.username_label)
        self.username_entry = QLineEdit()
        layout.addWidget(self.username_entry)

        self.password_label = QLabel("Password:")
        layout.addWidget(self.password_label)
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_entry)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_ssh)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

    def connect_to_ssh(self):
        hostname = self.hostname_entry.text()
        port = int(self.port_entry.text())
        username = self.username_entry.text()
        password = self.password_entry.text()

        try:
            self.ssh_client = SSHClient(hostname, port, username, password)
            self.ssh_client.connect()
            QMessageBox.information(self, "Success", "Connected to SSH server")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
