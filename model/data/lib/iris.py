from pathlib import Path
from model.data.static import BaseDataAccess
from dataclasses import dataclass, fields, asdict
from typing import Dict
import random
import csv
import hashlib
import json
from csv import DictReader

IRIS_FP=str(Path(__file__).parent) + '/raw/iris.csv'

# Can we dataclass this?
@dataclass
class IrisItem:
    """Object representation of a record of Iris data with types"""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    variety: str
        

class IrisDAO(BaseDataAccess):
    """Data Access Object wrapping the import of raw Iris data.

    Wraps the construction of a list of records of dataclass `IrisItem`
    along with helper methods to simplify downstream use of the datasest.
    If the source data being read in at 'fp' changes, `read_row` and 
    or `read_data` will need to be updated to adjust for the changes.

    All remaining code downstream should be designed to work based 
    on the `IrisItem` dataclass definition.
    """

    def __init__(self, fp):
        self.data = self.read_data(fp)
        self.first_record = self.data[0]
        self.fields = fields(self.first_record)
        self.size = len(self.data)
        self.data_checksum = self.checksum(self.data)

    def read_row(self, row: Dict):
        """Creates a `IrisItem` from a dict with appropriate keys
        and values.
        """
        record = IrisItem(sepal_length=row.get('sepal.length'),
                                sepal_width=row.get('sepal.width'),
                                petal_length=row.get('petal.length'),
                                petal_width=row.get('petal.width'),
                                variety=row.get('variety')
                                ) 
        return record

    def read_data(self, fp: str):
        """Wraps the import of multiple IrisItem objects by
        looping over a list of dicts and building out the
        list of objects. Object being imported is defined in
        the `IrisItem` dataclass which has a record based 
        read operation defined in `read_row`
        """
        data=[]
        with open(fp) as f:
            csv_dict_reader = DictReader(f)
            for row in csv_dict_reader:
                iris = self.read_row(row)
                data.append(iris)
        return data

    def checksum(self, data):
        data_md5 = hashlib.md5(json.dumps(str(data), sort_keys=True).encode('utf-8')).hexdigest()
        return data_md5

    def sample(self, size: int=1):
        """Random sample of the dataclass without replacement
        """
        return random.sample(self.data, size)

    def asjson(self):
        """Returns the dataset as a list of dictionaries instead
        of a list of dataclasses. This can sometimes be more 
        convenient to use.
        """
        return [asdict(item) for item in self.data]

    def describe():
        pass

    def validate(self, fp:str):
        """Validates that the data present in `self.data` is an
        exact match to the data being imported.
        """
        check_data = self.read_data(fp)
        check_hash = self.checksum(check_data)
        assert check_hash == self.checksum(self.data)

dataset = IrisDAO(IRIS_FP)
