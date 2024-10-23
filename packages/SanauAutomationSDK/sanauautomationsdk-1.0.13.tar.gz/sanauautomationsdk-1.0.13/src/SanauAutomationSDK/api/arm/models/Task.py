class Task:

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.title = kwargs['title']
        self.description = kwargs['description'] #dictionary
        self.addition = kwargs['addition']
        self.categories = kwargs['categories']
        self.comments = []
        self.status = 'new'
