import os
import shutil

from fastapi import UploadFile


class UploadBookFile:
    # upload file to static folder
    def __init__(self, file: UploadFile, book_id: int):
        self.file = file
        self.book_id = book_id

    def run(self):
        file_path = "static/file/" + str(self.book_id)+".{}".format(self.file.filename.split(".")[-1])

        if not os.path.exists("static/file"):
            os.mkdir("static/file")

        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(self.file.file, buffer)

        return True
