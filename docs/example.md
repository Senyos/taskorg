# Example [RU]

## Пример использования

```py
from backend.jsonstore import JSONStore
from backend.taskmanage import TaskManage

JStore = JSONStore("jsons/tasks.json")
TManage = TaskManage()


if __name__ == "__main__":
    subject, task, date = input("Enter subject, task and date:\n").split("|")
    TManage.create_task(subject, task, date)
    JStore.write_json(TManage.get_all_tasks())
    print(JStore.read_json())
```
