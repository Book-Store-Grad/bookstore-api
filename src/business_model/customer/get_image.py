import os
import shutil

from fastapi import UploadFile


class GetCustomerImage:
    def __init__(self, customer_id: int):
        self.customer_id = customer_id

    def run(self):
        directory = os.path.join("static", "customer")
        file_path = os.path.join(directory, str(self.customer_id) + ".{}".format("jpg"))

        if not os.path.exists(file_path):
            return None

        return file_path
