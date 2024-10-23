class Task:

    def __init__(self, task_id, title, description, addition, categories):
        self.id = task_id
        self.title = title
        self.description = description
        self.addition = addition
        self.categories = categories
        self.comments = []
        self.status = "new"
