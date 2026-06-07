from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Mem(models.Model):
    photo = models.ImageField(upload_to = 'photo_mem')
    title = models.CharField(max_length = 20)
    author_name = models.CharField(max_length=20)

    def __str__(self):
        return  self.title

    @property
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    mem = models.ForeignKey(Mem, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)



class User(AbstractUser):
    ROLE = (('user','Пользователь',),
            ('media', 'Блогер'),
            ('admin', 'Админ'))
    role = models.CharField(choices=ROLE, default='user' )

    def __str__(self):
        return self.username

class Like(models.Model):
    mem = models.ForeignKey(Mem, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'mem')

    def __str__(self):
        return f'{self.author.username} laked {self.mem.title}'

class Subscribes(models.Model):
    sub = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='sub')
    suber = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('sub', 'suber')
    def __str__(self):
        return f'{self.sub.username} subscribed {self.suber.title}'