from typing import List, Tuple

class TaskManage():
    """TaskManage provides some functions to
    manage tasks.
    """
    def __init__(self) -> None:
        """Initializes self._subject: dict which provides
        shortened and full names of all the subjects.
        Also there's self._tasks: List[dict].
        """
        # self._subjects: dict = {
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

    def create_task(self, subject: str, 
                    task: str, date: str) -> None:
        """Getting subject: str, task: str and date: str
        on enter and if the subject exist in self._subjects
        then creates a dict of task and addes it into
        self._tasks: List[dict].
        """
        #if subject in self._subjects:
        #subject = self._subjects[subject]
        self._tasks.append({
                                "Subject": subject,
                                "Task": task,
                                "Date-when-do": date
                            })

        return None
        #else:
        #print("Error: there's no such a subject.")

    def set_tasks(self, tasks:List[dict]=[]) -> None:
        """Set self._tasks = tasks."""
        self._tasks = tasks.copy()

        return None

    def get_all_tasks(self) -> List[dict]:
        """Returns self._tasks tasks that List[dict]."""
        return self._tasks
    
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
        or `Subject' str, `value' -- value of `by'.  
        `Date' = `2025-12-15' str, `Subject' must be 
        the name of some subjects.  Returns `tuple' of `ints'.
        """
        byes = ["Date", "Subject"]

        if not by in byes:
            pass
        elif by == byes[0]:
            by = "Date-when-do"

        _indexes: list = []

        for i, dict_ in enumerate(self._tasks):
            if dict_[by] == value:
                _indexes.append(i)

        return tuple(_indexes)

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
