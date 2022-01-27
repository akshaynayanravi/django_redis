from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class TaskStatus(models.TextChoices):
    COMPLETED = "CO", "Completed"
    PENDING = "PE", "Pending"
    DROPPED = "DR", "Dropped"


class Tasks(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    deadline = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2
    )
