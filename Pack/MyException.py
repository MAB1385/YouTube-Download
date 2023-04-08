#Raising Exceptions:
class DataException(Exception):
    """A class for managing data type errors."""
    def __init__(self, text) -> None:
        super().__init__(text)
        self.__text=text

    def __str__(self) -> str:
        return f'Error: {self.__text}...'