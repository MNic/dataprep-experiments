from pathlib import Path
from model.data.static import BaseDataAccess
from dataclasses import dataclass, fields, asdict
from typing import Dict
import random
import csv
from csv import DictReader

IRIS_FP=str(Path(__file__).parent) + '/raw/iris.csv'

# Can we dataclass this?
@dataclass
class IrisItem:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    variety: str
        

class IrisDAO(BaseDataAccess):

    def __init__(self, fp):
        self.data = self.read_data(fp)
        self.first_record = self.data[0]
        self.fields = fields(self.first_record)
        self.size = len(self.data)

    def read_row(self, row: Dict):
        record = IrisItem(sepal_length=row.get('sepal.length'),
                                sepal_width=row.get('sepal.width'),
                                petal_length=row.get('petal.length'),
                                petal_width=row.get('petal.width'),
                                variety=row.get('variety')
                                ) 
        return record

    def read_data(self, fp: str):
        data=[]
        with open(fp) as f:
            csv_dict_reader = DictReader(f)
            for row in csv_dict_reader:
                iris = self.read_row(row)
                data.append(iris)
        return data

    def sample(self, size: int=1):
        # Random sample without replacement
        return random.sample(self.data, size)

    def asjson(self):
        return [asdict(item) for item in self.data]

    def describe():
        pass

    def validate():
        pass

dataset = IrisDAO(IRIS_FP)
