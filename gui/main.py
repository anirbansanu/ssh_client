from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QMenu, QMenuBar
from PyQt5.QtGui import QIcon
from gui.sftp_gui import SFTPWindow
from gui.ssh_gui import SSHWindow
from gui.terminal_emulation import TerminalEmulationWindow
from gui.tunneling_gui import TunnelingWindow

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced SSH Client")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon('assets/icons/ssh_client_icon.png'))

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.apply_stylesheet_from_files()
        self.create_menu()

    def apply_stylesheet(self):
        stylesheet = """
        QMainWindow {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        QTabWidget::pane {
            border: 1px solid #34495e;
            background: #34495e;
        }
        QTabBar::tab {
            background: #34495e;
            color: #ecf0f1;
            padding: 10px;
            border: 1px solid #34495e;
            border-bottom: none;
        }
        QTabBar::tab:selected, QTabBar::tab:hover {
            background: #1abc9c;
            color: #2c3e50;
        }
        QTabBar::close-button {
            image: url(assets/icons/close-icon.png);
            subcontrol-position: right;
        }
        QTabBar::close-button:hover {
            image: url(assets/icons/close-icon-hover.png);
        }
        QLabel {
            color: #ecf0f1;
            font-weight: bold;
        }
        QLineEdit {
            background: #2c3e4f;
            color: #ecf0f1;
            border: 2px solid #2c3e50;
            padding: 5px;
            border-radius: 5px;
        }

        QLineEdit:focus {
            border: 2px solid #1abc9c;
        }
        QPushButton {
            background: #1abc9c;
            color: #2c3e50;
            border: 1px solid #16a085;
            padding: 10px;
        }
        QPushButton:hover {
            background: #16a085;
        }
        QMenuBar {
            background: #34495e;
            color: #ecf0f1;
        }
        QMenuBar::item {
            background: #34495e;
            color: #ecf0f1;
        }
        QMenuBar::item:selected {
            background: #1abc9c;
            color: #2c3e50;
        }
        QMenu {
            background: #34495e;
            color: #ecf0f1;
        }
        QMenu::item:selected {
            background: #1abc9c;
            color: #2c3e50;
        }
        
        """
        self.tabs.setStyleSheet(stylesheet)

    def apply_stylesheet_from_files(self):
        with open("assets/styles/styles.css", "r") as f:
            self.setStyleSheet(f.read())

    def create_menu(self):
        menu_bar = self.menuBar()

        # SSH Menu
        ssh_menu = menu_bar.addMenu("SSH")
        open_ssh = QAction("Open SSH Client", self)
        open_ssh.triggered.connect(self.open_ssh_window)
        ssh_menu.addAction(open_ssh)

        # SFTP Menu
        sftp_menu = menu_bar.addMenu("SFTP")
        open_sftp = QAction("Open SFTP Client", self)
        open_sftp.triggered.connect(self.open_sftp_window)
        sftp_menu.addAction(open_sftp)

        # Terminal Emulation Menu
        terminal_menu = menu_bar.addMenu("Terminal Emulation")
        open_terminal = QAction("Open Terminal", self)
        open_terminal.triggered.connect(self.open_terminal_emulation_window)
        terminal_menu.addAction(open_terminal)

        # Tunneling Menu
        tunneling_menu = menu_bar.addMenu("Tunneling")
        open_tunneling = QAction("Open Tunneling", self)
        open_tunneling.triggered.connect(self.open_tunneling_window)
        tunneling_menu.addAction(open_tunneling)

    def open_sftp_window(self):
        self.sftp_window = SFTPWindow()
        self.tabs.addTab(self.sftp_window, "SFTP Client")

    def open_ssh_window(self):
        self.ssh_window = SSHWindow()
        self.tabs.addTab(self.ssh_window, "SSH Client")

    def open_terminal_emulation_window(self):
        self.terminal_window = TerminalEmulationWindow()
        self.tabs.addTab(self.terminal_window, "Terminal Emulation")

    def open_tunneling_window(self):
        self.tunneling_window = TunnelingWindow()
        self.tabs.addTab(self.tunneling_window, "Tunneling")

    def close_tab(self, index):
        widget = self.tabs.widget(index)
        if widget:
            widget.deleteLater()
        self.tabs.removeTab(index)

if __name__ == "__main__":
    app = QApplication([])
    window = MainApplication()
    window.show()
    app.exec_()
