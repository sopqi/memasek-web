from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from PIL import Image  # ДОБАВИТЬ ЭТОТ ИМПОРТ


class Mem(models.Model):
    photo = models.ImageField(upload_to='photo_mem')
    title = models.CharField(max_length=20)
    author_name = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            try:
                filepath = self.photo.path
                img = Image.open(filepath)

                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                if img.height > 800 or img.width > 800:
                    output_size = (800, 800)
                    img.thumbnail(output_size)

                img.save(filepath, format='JPEG', quality=75, optimize=True)
            except Exception as e:
                pass


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