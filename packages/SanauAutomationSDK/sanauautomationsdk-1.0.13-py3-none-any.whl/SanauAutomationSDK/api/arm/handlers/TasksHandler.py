from ...Wrapper import Wrapper
from ....utils.logutils import logger
from ..models.Task import Task

from typing import Callable


class TasksHandler:

    def __init__(self, api_wrapper: Wrapper):
        self.api_wrapper = api_wrapper

    def execute_tasks(self, load_bank_statement: Callable, status="last_task"):
        tasks = self._get_tasks(status)

        if len(tasks):
            if type(tasks) == str:
                logger.info(tasks)
                return True

            for task in tasks:
                logger.info("Начал таск " + str(task.id))
                if task.addition and task.categories:
                    database_id = task.addition["database_id"]

                    for category in task.categories.values():
                        if category['name'] == "Загрузить выписку":
                            for update, status in load_bank_statement(database_id, task):
                                if status == 'waiting':
                                    self.update_status(task=task, status='waiting')
                                    self.comment(task=task, text=update, tag='warning')
                                    continue
                                self.comment(task=task, text=update)
                                continue
                            if task.status != 'waiting':
                                self.update_status(task=task, status='completed')
                else:
                    self.update_status(task=task, status='waiting')
                    self.comment(task=task, text="Нет описания задачи или категории.")
                    continue
                logger.info("Перебраны таски.")
                return True

        else:
            return False

    def _get_tasks(self, status):
        tasks = []

        try:
            if status != 'last_task':
                json_tasks = self.api_wrapper.get_last_new_task()
                if 'message' in json_tasks.keys():
                    return json_tasks['message']
                return [Task(**json_tasks)]
            else:
                json_tasks = self.api_wrapper.get_tasks_by_status(status)
                for props in json_tasks:
                    if props:
                        addition = props["addition"] if props["addition"] else {}
                        categories = props["categories"] if props["categories"] else {}
                        task = Task(id=props["id"], title=props["title"], description=props["description"],
                                    addition=addition, categories=categories)
                        self.update_status(task=task, status="in_progress")
                        print("Начал таск с id: ", task.id)
                        tasks.append(task)
                        break

                return tasks
        except Exception as e:
            logger.error(f"Не удается выгрузить таски из АРМа с ошибкой: {e}")
            return []

    def update_status(self, task, status):
        task.status = status

        try:
            self.api_wrapper.update_task_status(task_id=task.id, params={'status': status})
        except Exception as e:
            logger.error(f"Не удается обновить статус таска с ошибкой: {e}")

    def comment(self, task, text, tag=None):
        try:
            self.api_wrapper.post_task_comment(task_id=task['id'], params={'text': text, 'tag': tag})
        except Exception as e:
            logger.error(f"Не удается оставить комментарий к таску с ошибкой: {e}")
