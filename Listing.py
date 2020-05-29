from abc import ABC, abstractmethod


class Listing(ABC):

    # abstract method
    def noofsides(self):
        pass

    def check_ButtonArray(self):
        if self.check_ButtonArray is None:
            raise NotImplementedError('Subclasses must define Button Array')
