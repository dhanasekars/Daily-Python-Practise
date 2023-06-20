
"""
Created by: DS
Created at: 2023-06-20 12:50:53

This is to learn about watchdog package

"""
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define a custom event handler 

class FileEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created' or event.event_type == 'modified':
            print("File changed", event.src_path)
            
directory_to_watch = '/Users/ds/Library/Mobile Documents/com~apple~CloudDocs/Second Brain/'

observer = Observer()

observer.schedule(FileEventHandler(),path=directory_to_watch, recursive=True)

observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
    
observer.join()
