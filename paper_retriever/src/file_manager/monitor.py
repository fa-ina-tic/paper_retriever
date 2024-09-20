import glob
import os
import time
from typing import List

from watchdog.observers import Observer
from watchdog.events import (FileMovedEvent,
							FileCreatedEvent,
							FileDeletedEvent,
							FileModifiedEvent,
							FileSystemEventHandler)

class EventHandler(FileSystemEventHandler):
	def __init__(self, dir_path:str):
		super().__init__()
		self.file_list:List[str] = glob.glob(dir_path + '/*', recursive=True)
		self.workplace:str = os.curdir

	def on_moved(self, event: FileMovedEvent):
		if not event.is_directory:
			rel_path:bytes = os.path.relpath(event.src_path, self.workplace)
			self.file_list.remove(rel_path)

	def on_created(self, event: FileCreatedEvent):
		if not event.is_directory:
			rel_path:bytes = os.path.relpath(event.src_path, self.workplace)
			self.file_list.append(rel_path)

	def on_deleted(self, event: FileDeletedEvent):
		if not event.is_directory:
			rel_path:bytes = os.path.relpath(event.src_path, self.workplace)
			self.file_list.remove(rel_path)

	def on_modified(self, event: FileModifiedEvent):
		if not event.is_directory:
			rel_path:bytes = os.path.relpath(event.src_path, self.workplace)
			print(rel_path, "modified")

class DirMonitor:
	def __init__(self, dir_path:str, handler):
		self.handler:FileSystemEventHandler = handler(dir_path)
		self.dir_path:str = dir_path

	def run(self,):
		observer = Observer()
		observer.schedule(self.handler, self.dir_path ,recursive=True)
		observer.start()
		try:
			while True:
				print(self.handler.file_list)
				time.sleep(5)
		finally:
			observer.stop()
			observer.join()

if __name__ == "__main__":
	dir_path = "data"
	watcher = DirMonitor(dir_path, EventHandler)
	watcher.run()