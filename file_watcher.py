import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from loguru import logger

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, app, excluded_files=None):
        super().__init__()
        self.app = app
        self.excluded_files = excluded_files or []

    def on_any_event(self, event):
        if event.is_directory:
            return None

        if event.src_path in self.excluded_files:
            return None
        else:
            print(f'File modified: {event.src_path}')
        self.app.exit(100)  # Exit with a specific code to indicate a reload is needed

def watch_files(app, excluded_files=None):
    event_handler = FileChangeHandler(app, excluded_files)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            app.processEvents()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        logger.info('Watcher terminated by keyboard interrupt.')
        sys.exit(0)
