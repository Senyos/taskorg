class TaskManage():
    """TaskManage provides some functions to
    manage tasks.
    """
    def __init__(self):
        """Initializes self._subject: dict which provides
        shortened and full names of all the subjects.
        Also there's self._tasks: list[dict, ...].
        """
        self._subjects: dict = {
                                   "Math": "Mathematics",
                                   "Phys": "Physics",
                                   "Hist": "History",
                                   "Tech": "ProgTech",
                                   "Py": "ProgPy",
                                   "IT": "IT",
                                   "Eng": "English",
                                   "Phil": "Philosophy" 
                               }
        self._tasks: list[dict, ...] = []

    def create_task(self, subject: str, 
                    task: str, date: str) -> None:
        """Getting subject: str, task: str and date: str
        on enter and if the subject exist in self._subjects
        then creates a dict of task and addes it into
        self._tasks: list[dict, ...].
        """
        if subject in self._subjects:
            subject = self._subjects[subject]
            self._tasks.append({
                                   "Subject": subject,
                                   "Task": task,
                                   "Date-when-do": date
                               })

        else:
            print("Error: there's no such a subject.")

    def get_all_tasks(self) -> list[dict, ...]:
        return self._tasks

    def delete_last_task(self) -> None:
        """Deleting one last task of the list self._tasks."""
        try:
            self._tasks.pop()
        except:
            print("There's no tasks already.")

    def clear_tasks(self) -> None:
        """Erase all the tasks in the list"""
        self._tasks.clear()
