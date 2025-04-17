############################################################
#                                                          #
# A program licensed by The MIT License. 2025 DjBlooky (c) #
#           https://github.com/Senyos/taskorg              #
#                                                          #
############################################################

from typing import List, Tuple

class TaskManage():
    """TaskManage provides some functions to
    manage tasks.
    """
    def __init__(self) -> None:
        """Initializes self._themes: dict which provides
        shortened and full names of all the themes.
        Also there's self._tasks: List[dict].
        """
        # self._themes: dict = {
        #                            "Math": "Mathematics",
        #                            "Phys": "Physics",
        #                            "Hist": "History",
        #                            "Tech": "ProgTech",
        #                            "Py": "ProgPy",
        #                            "IT": "IT",
        #                            "Eng": "English",
        #                            "Phil": "Philosophy" 
        #                        }
        self._tasks: List[dict] = []

        return None

    def create_task(self, theme: str, 
                    note: str, date: str) -> None:
        """Getting theme: str, note: str and date: str
        on enter and if the theme exist in self._themes
        then creates a dict of task and addes it into
        self._tasks: List[dict].
        """
        #if theme in self._themes:
        #theme = self._themes[theme]
        self._tasks.append({
                                "Theme": theme,
                                "Note": note,
                                "Date-when-do": date
                            })

        return None
        #else:
        #print("Error: there's no such a theme.")

    def set_tasks(self, tasks:List[dict]=[]) -> None:
        """Set self._tasks = tasks."""
        self._tasks = tasks.copy()

        return None

    def get_all_tasks(self) -> List[dict]:
        """Returns self._tasks tasks that List[dict]."""
        return self._tasks

    def get_all_tasks_pretty(self) -> str:
        """Returns self._tasks pretty and `str',
        if empty, returns empty `str'"""
        if self._tasks:
            _text = ''
            for i in self._tasks:
                _theme = i["Theme"]
                _note = i["Note"]
                _date = i["Date-when-do"]

                _text = _text + f'Тема: {_theme}\nЗаметка: {_note}\nДата: {_date}\n\n'
            
            return _text
        else:
            return ''
    
    # FIXME: duplicate elements when indexes are negative numbers.
    def get_tasks_by_indexes(self, 
                             tasks_to_get:Tuple[int]=()) -> List[dict]:
        """Returns tasks by their indexes."""
        _tasks_by_indexes:List[dict] = []

        for i in tasks_to_get:
            _tasks_by_indexes.append(self._tasks[i])
        
        return _tasks_by_indexes

    def find_tasks_indexes(self, by:str="Date", 
                           value:str="2025-12-15") -> Tuple[int]:
        """Finding tasks. `by' -- Filter that can be `Date' 
        or `Theme' or 'Note' str, `value' -- value of `by'.  
        `Date' = `2025-12-15' str, `Theme' must be 
        the name of some themes.  Returns `tuple' of `ints'.
        """
        byes = ["Date", "Theme", "Note"]

        if not by in byes:
            pass
        elif by == byes[0]:
            by = "Date-when-do"

        _indexes: list = []

        # ~~If searching by content~~ OLD COMMENT
        for i, dict_ in enumerate(self._tasks):
            if dict_[by].find(value) >= 0:
                _indexes.append(i)
        
        return tuple(_indexes)

        # OLD WAY
        # else:
        #     for i, dict_ in enumerate(self._tasks):
        #         if dict_[by] == value:
        #             _indexes.append(i)

        #     return tuple(_indexes)

    def save_tasks(self, tasks_to_save:Tuple[int]=()) -> None:
        """Removing all the tasks that are not
        tasks_to_save indexes from self._tasks.  
        Returns `NoneType'.
        """
        _new_tasks_list:List[dict] = []
        if tasks_to_save:
            for i, v in enumerate(self._tasks):
                if i in tasks_to_save:
                    _new_tasks_list.append(v)
            self._tasks = _new_tasks_list.copy()
        else:
            self._tasks = []

    def delete_tasks(self, tasks_to_delete:Tuple[int]=()) -> None:
        """Removing all the tasks_to_delete indexes from self._tasks.  
        Returns `NoneType'.
        """
        _new_tasks_list:List[dict] = []
        if tasks_to_delete:
            for i, v in enumerate(self._tasks):
                if i in tasks_to_delete:
                    continue
                _new_tasks_list.append(v)
            self._tasks = _new_tasks_list.copy()
                
        return None

    def delete_last_task(self) -> None:
        """Deleting one last task of the list self._tasks."""
        try:
            self._tasks.pop()
        except:
            pass
        
        return None

    def clear_tasks(self) -> None:
        """Erase all the tasks in the list"""
        self._tasks.clear()

        return None
