from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=30, verbose_name='Имя')

    def __str__(self):
        return self.user_name


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    data_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text
