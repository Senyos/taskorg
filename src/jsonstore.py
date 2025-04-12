import json


class JSONStore():
    """Class with various functions to do
    different manipulation with json files.
    """
    def __init__(self, file: str):
        """Init with `file' argument given. 
        `file' needs to be `str' //path//to//file.
        
        """
        self._file = file

    def read_json(self) -> list[dict, ...]:
        """Reading json `file' given and
        returns json.load() -- `list' of `dicts':
        list[dict, ...]."""
        with open(self._file, "r", 
                  encoding="utf-8") as _f:
            return json.load(_f)

    def write_json(self, 
                   new_data: list[dict, ...]) -> None:
        """Writes given `new_data' list[dict, ...] 
        to `file' with replacing everything
        that was in file before. Returns None.
        """
        with open(self._file, "w", 
                  encoding="utf-8") as _f:
            json.dump(new_data, _f)
