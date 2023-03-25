from enum import Enum
from typing import Union

from databaser.data_model import DataModel
from databaser.engine.result import ExecutionResult

from src.exception.database_object_exists import DatabaseObjectExists


class ModelType(str, Enum):
    insert = 'INSERT'
    read = 'READ'
    update = 'UPDATE'
    delete = 'DELETE'


class BusinessModel:
    def __init__(self, model: DataModel, model_type: ModelType, check_exists: dict = None):
        if check_exists is None:
            check_exists = {}

        self.model = model
        self.model_type = model_type

        self.check_exists = check_exists

    def run(self, data: dict = None, conditions: dict = None) -> Union[None, ExecutionResult]:

        if not data and self.model_type.value in [ModelType.insert, ModelType.update]:
            raise Exception("Data field is missing")

        if self.check_exists:
            exists = self.model.get_one(condition=self.check_exists).show(True).result
            print("Checking Exists")
            if exists:
                raise DatabaseObjectExists()

            del exists

        if self.model_type.value in [ModelType.insert]:
            insert = self.model.insert(data=data).get_one(order_by={self.model.fields[0].name: "DESC"})
            print("INSERT SQL:", insert.get_transactions())
            return insert.show(True)

        if not conditions:
            raise Exception("Conditions field is missing")

        if self.model_type.value == ModelType.update:
            return self.model.update(
                data=data,
                conditions=conditions,
            ).get_one(condition=conditions, order_by={self.model.fields[0].name: "DESC"}).show(True)

        if self.model_type.value == ModelType.delete:
            return self.model.delete(
                data=data,
                conditions=conditions,
            ).commit()

        return None
