from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
from core.ssh_client import SSHClient

class SSHWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SSH Client")
        self.setGeometry(100, 100, 800, 600)

        self.ssh_client = None

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

        self.command_entry = QLineEdit()
        self.command_entry.setPlaceholderText("Enter command to execute")
        layout.addWidget(self.command_entry)

        self.execute_button = QPushButton("Execute Command")
        self.execute_button.clicked.connect(self.execute_command)
        layout.addWidget(self.execute_button)

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

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

    def execute_command(self):
        command = self.command_entry.text()
        if self.ssh_client:
            try:
                output = self.ssh_client.execute_command(command)
                self.output_area.append(f"$ {command}\n{output}\n")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Warning", "Not connected to any SSH server")
