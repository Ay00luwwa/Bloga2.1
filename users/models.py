from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='./media/default.jpg', upload_to='profile_pics')  
    bio = models.TextField(blank=True, max_length=500)  
    email = models.EmailField(unique=True, null=True, blank=True)
    location = models.CharField(blank=True, max_length=100)  
    birth_date = models.DateField(null=True, blank=True) 
    website = models.URLField(blank=True, max_length=200)  

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new:
            img = Image.open(self.image.path)
            if img.height > 450 or img.width > 450:
                output_size = (450, 450)
                img.thumbnail(output_size)
                img.save(self.image.path)
