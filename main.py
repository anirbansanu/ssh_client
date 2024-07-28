import sys
import subprocess
from PyQt5.QtWidgets import QApplication
from gui.main import MainApplication
from file_watcher import watch_files
from loguru import logger

log_file = "app.log"
logger.add(log_file, rotation="500 MB")  # Log to a file with rotation

def run_application():
    while True:
        logger.info("Starting application...")
        app = QApplication(sys.argv)
        window = MainApplication()
        window.show()

        # Start the file watcher in a separate thread
        watch_files(app, excluded_files=[log_file])

        exit_code = app.exec_()

        if exit_code == 100:
            logger.info("Changes detected. Restarting application...")
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()
        else:
            logger.info("Exiting application...")
            break

if __name__ == "__main__":
    run_application()
