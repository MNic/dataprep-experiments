from abc import ABC, abstractmethod

class BaseDataAccess(ABC):
    """An object representing a complex unit of data for analysis. 

    Typically a csv import, dataframe, or other array-like object
    """

    @abstractmethod
    def describe():
        pass

    @abstractmethod
    def validate():
        pass
