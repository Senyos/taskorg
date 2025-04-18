############################################################
#                                                          #
# A program licensed by The MIT License. 2025 DjBlooky (c) #
#           https://github.com/Senyos/taskorg              #
#                                                          #
############################################################

import json
from typing import List


class JSONStore():
    """Class with various functions to do
    different manipulation with json files.
    """
    def __init__(self, file: str) -> None:
        """Init with `file' argument given. 
        `file' needs to be `str' //path//to//file.
        
        """
        self._file = file

        return None

    def read_json(self) -> List[dict]:
        """Reading json `file' given and
        returns json.load() -- `list' of `dicts':
        List[dict]."""
        with open(self._file, "r", 
                  encoding="utf-8") as _f:
            return json.load(_f)

    def write_json(self, 
                   new_data: List[dict]) -> None:
        """Writes given `new_data' List[dict] 
        to `file' with replacing everything
        that was in file before. Returns None.
        """
        # Delete duplicates
        _seen = set()
        new_data = [dict_ for dict_ in new_data if tuple(dict_.items()) 
        not in _seen and not _seen.add(tuple(dict_.items()))]

        with open(self._file, "w", 
                  encoding="utf-8") as _f:
            json.dump(new_data, _f, indent=4)
        return None
