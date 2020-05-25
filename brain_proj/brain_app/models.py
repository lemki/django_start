from django.db import models


class Post(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.pub_date} : {self.text}'


class Blog(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

