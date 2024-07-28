from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from gui.sftp_gui import SFTPWindow
from gui.ssh_gui import SSHWindow

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SSH Client")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.sftp_button = QPushButton("SFTP Client")
        self.sftp_button.clicked.connect(self.open_sftp_window)
        layout.addWidget(self.sftp_button)

        self.ssh_button = QPushButton("SSH Client")
        self.ssh_button.clicked.connect(self.open_ssh_window)
        layout.addWidget(self.ssh_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_sftp_window(self):
        self.sftp_window = SFTPWindow()
        self.sftp_window.show()

    def open_ssh_window(self):
        self.ssh_window = SSHWindow()
        self.ssh_window.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainApplication()
    window.show()
    app.exec_()
