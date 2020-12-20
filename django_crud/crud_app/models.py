from django.db import models
from django.urls import reverse
from django.conf import settings


class Project(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spid = models.CharField(max_length=1000)  # is sid + '_' + pid , to quickly identify projects created by a certain user without using complex queries
    sid = models.CharField(max_length=1000)  # the id of the user
    pid = models.CharField(max_length=1000)  # the id of the project
    # name = models.CharField(max_length=200)
    name = models.CharField(max_length=1000)
    storeUrl = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_fbv_user:book_edit', kwargs={'pk': self.pk})
