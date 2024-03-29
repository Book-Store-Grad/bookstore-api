import os
import shutil

from fastapi import UploadFile


class GetBookImage:
    def __init__(self, book_id: int):
        self.book_id = book_id

    def run(self):
        file_path = os.path.join("static", str(self.book_id) + ".jpg")

        if not os.path.exists(file_path):
            return None

        return file_path
