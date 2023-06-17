from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
