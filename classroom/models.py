from django.db import models

# Create your models here.
class Teacher(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    sub_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name} teaches {self.sub_name}"
