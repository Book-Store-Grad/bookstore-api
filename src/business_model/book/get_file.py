import os
import shutil

from fastapi import UploadFile


class GetBookFile:
    def __init__(self, book_id: int):
        self.book_id = book_id

    def run(self):
        file_path = os.path.join(os.path.join("static", "file"), str(self.book_id) + ".pdf")

        if not os.path.exists(file_path):
            return None

        return file_path
