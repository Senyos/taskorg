# Example [RU]

## ВНИМАНИЕ

Недействительная документация.

## Пример использования

```py
# Создается список заданий случайным образом, а затем фильтруется по значению даты, после чего удаляются задания, совпадающие с указанной датой.
from backend.jsonstore import JSONStore
from backend.taskmanage import TaskManage
from random import randint
from pprint import pprint
import os

JStore = JSONStore("./jsons/tasks.json")
TManage = TaskManage()


if __name__ == "__main__":
    # for relative paths works
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    subjects = ["Math", "Philosophy",
                "Physics", "Programming"]
    tasks = ["p. 12, ex 1, 2", "p. 7, ex 2", 
             "p. 1, ex 8", "p. 5, ex 3, 4"]
    dates = ["2025-04-10", "2025-03-05",
             "2025-07-15", "2025-05-01",
             "2025-05-11", "2025-06-13",]

    for i in range(15):
        subject, task, date = subjects[randint(0, 3)], tasks[randint(0, 3)], dates[randint(0, 5)] #input("Enter subject, task and date:\n").split("|")
        TManage.create_task(subject, task, date)

    JStore.write_json(TManage.get_all_tasks())

    json_data = JStore.read_json()
    pprint(json_data)
    print()

    TManage.set_tasks(json_data)

    indexes = TManage.find_tasks_indexes("Date", "2025-06-13")
    TManage.delete_tasks(indexes)

    json_data = TManage.get_all_tasks()

    pprint(json_data)
```
