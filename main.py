import sys
import subprocess
from PyQt5.QtWidgets import QApplication
from gui.main import MainApplication
from file_watcher import watch_files

def run_application():
    while True:
        app = QApplication(sys.argv)
        window = MainApplication()
        window.show()

        # Start the file watcher in a separate thread
        watch_files(app)

        exit_code = app.exec_()

        if exit_code != 100:
            break
        else:
            # Relaunch the application
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()

if __name__ == "__main__":
    run_application()
