from django.db import models
from django.urls import reverse
from django.conf import settings


class Project(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spid = models.CharField()  # is sid + '_' + pid , to quickly identify projects created by a certain user without using complex queries
    sid = models.CharField()  # the id of the user
    pid = models.CharField()  # the id of the project
    # name = models.CharField(max_length=200)
    name = models.CharField()
    storeUrl = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_fbv_user:book_edit', kwargs={'pk': self.pk})
