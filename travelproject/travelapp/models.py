from django.db import models
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    t_img = models.ImageField(upload_to='pics')
    t_name = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.t_name
# Create your models here.
