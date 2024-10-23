from ...Wrapper import Wrapper
from ..models.Task import Task
from ....utils.logutils import logger


import yaml


class TasksHandler:

    def __init__(self, api_wrapper: Wrapper):
        self.api_wrapper = api_wrapper

    def get_my_new_tasks(self):
        try:
            json = self.api_wrapper.get_my_new_tasks()
            return [Task(task_id=props["id"], title=props["title"], description=props["description"],
                         addition=props["addition"], categories=props["categories"]) for props in json]
        except Exception as e:
            logger.error(f"Не удается выгрузить таски из АРМа с ошибкой: {e}")
            return []

    def get_the_last_task_bot(self):
        try:
            json = self.api_wrapper.get_last_new_task()
            if "message" in json.keys():
                return json["message"]
            return Task(task_id=json["id"], title=json["title"], description=json["description"],
                        addition=json["addition"], categories=json["categories"])
        except Exception as e:
            logger.error(f"Не удается выгрузить таски из АРМа с ошибкой: {e}")
            return []

    def get_all_tasks_bot(self, status=None):
        tasks = []

        try:
            if status:
                result = self.api_wrapper.get_tasks_by_status()
            else:
                result = self.api_wrapper.get_tasks()

            for props in result:
                if props:
                    addition = props["addition"] if props["addition"] else {}
                    categories = props["categories"] if props["categories"] else {}
                    task = Task(task_id=props["id"], title=props["title"], description=props["description"],
                                addition=addition, categories=categories)

                    tasks.append(task)
                    break
            return tasks
        except Exception as e:
            logger.error(f"Не удается выгрузить таски из АРМа с ошибкой: {e}")
            return []

    def get_my_new_tasks_bot(self):
        return self.get_all_tasks_bot(status="new")

    def get_in_progress_tasks_bot(self):
        return self.get_all_tasks_bot(status="in_progress")

    def get_waiting_tasks_bot(self):
        return self.get_all_tasks_bot(status="waiting")

    def get_completed_tasks_bot(self):
        return self.get_all_tasks_bot(status="completed")

    def get_checking_tasks_bot(self):
        return self.get_all_tasks_bot(status="checking")

    def get_checked_tasks_bot(self):
        return self.get_all_tasks_bot(status="checked")

    def delete_all_comments_in_task_bot(self, task):
        self.api_wrapper.delete_all_task_comments(task_id=task.id)
        return f"Удалены комментарии в таске №{task.id}"

    def resolve_task_param(self, task, param):
        try:
            parsed = yaml.load(task.description)
            return parsed[param]
        except KeyError:
            error_message = f"Не удается считать параметр {param} из описания таска"
            logger.error(error_message)

            if task.comments[-1]["text"] != error_message:
                self.set_comment(task=task, text=error_message)

            return None

    def update_task_status(self, task, status):
        task.status = status
        try:
            self.api_wrapper.update_task_status(task_id=task.id, status=status)
            return task
        except Exception as e:
            logger.error(f"Не удается обновить статус таска с ошибкой: {e}")

    def set_comment(self, task, text, tag=None):
        try:
            self.api_wrapper.post_task_comment(task_id=task.id, params={'text': text, 'tag': tag})
        except Exception as e:
            logger.error(f"Не удается оставить комментарий к таску с ошибкой: {e}")