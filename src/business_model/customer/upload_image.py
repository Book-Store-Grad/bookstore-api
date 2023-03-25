import os
import shutil

from fastapi import UploadFile


class UploadImage:
    # upload image to static folder
    def __init__(self, image: UploadFile, customer_id: int):
        self.image = image
        self.customer_id = customer_id

    def run(self):
        directory = os.path.join("static", "customer")
        file_path = os.path.join(directory, str(self.customer_id) + ".{}".format("jpg"))

        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(self.image.file, buffer)

        return True
