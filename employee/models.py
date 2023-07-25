from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Clock(models.Model):
    slug = models.SlugField()
    is_published = models.BooleanField(default=True)
    entry_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.user

# Para trabalhar com imagens
# poetry add Pillow
# img = models.ImageField(upload_to='employee/imgs/%Y/%m/%d/')
