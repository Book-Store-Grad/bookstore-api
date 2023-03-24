import os
import shutil

from fastapi import UploadFile


class UploadImage:
    # upload image to static folder
    def __init__(self, image: UploadFile, book_id: int):
        self.image = image
        self.book_id = book_id

    def run(self):
        file_path = "static/" + str(self.book_id)+".{}".format(self.image.filename.split(".")[-1])

        if not os.path.exists("static"):
            os.mkdir("static")

        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(self.image.file, buffer)

        return True
