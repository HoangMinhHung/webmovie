from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class MovieUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null = True)

class Profile(models.Model):
    user = models.OneToOneField(MovieUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
