from todos import models


class TodoStatus(models.TextChoices):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'