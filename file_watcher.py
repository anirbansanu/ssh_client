import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtWidgets import QApplication

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def on_modified(self, event):
        print(f'File modified: {event.src_path}')
        self.app.exit(100)  # Exit with a specific code to indicate a reload is needed

    def on_created(self, event):
        print(f'File created: {event.src_path}')
        self.app.exit(100)  # Exit with a specific code to indicate a reload is needed

    def on_deleted(self, event):
        print(f'File deleted: {event.src_path}')
        self.app.exit(100)  # Exit with a specific code to indicate a reload is needed

def watch_files(app):
    event_handler = FileChangeHandler(app)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            app.processEvents()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
