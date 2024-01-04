from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    TECH = 'Tech'
    AGRICULTURE = 'Agriculture'
    HEALTH = 'Health'
    FITNESS = 'Fitness'
    FOOD = 'Food'
    TRAVEL = 'Travel'
    SPORTS = 'Sports'
    SCIENCE = 'Science'
    GAMING = 'Gaming'
    BOOKS = 'Books'
    MEDIA = 'Media' 
    TV = 'TV'
    RELIGION = 'Religion'
    PETS = 'Pets'
    ANIMALS = 'Animals'
    CARS  = 'Cars'
    FASHION = 'Fashion'
    ANIME = 'Anime'
    HISTORY = 'History'
    OTHERS = 'Others'
    
    CATEGORY_CHOICES = [
        (TECH, 'Tech'),
        (AGRICULTURE, 'Agriculture'),
        (HEALTH , 'Health and Fitness'),
        (FOOD, 'Food'),
        (TRAVEL, 'Travel'),
        (SPORTS, 'Sports'),
        (SCIENCE, 'Science'),
        (GAMING, 'Gaming'),
        (BOOKS, 'Books'),
        (MEDIA, 'Media'),
        (TV, 'TV'),
        (RELIGION, 'Religion'),
        (PETS, 'Pets'),
        (ANIMALS, 'Animals'),
        (CARS, 'Cars'),
        (FASHION, 'Fashion'),
        (ANIME, 'Anime'),
        (HISTORY, 'History'),
        (OTHERS, 'Others'),     
    ]
    name = models.CharField(max_length=100, unique=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', default='default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    dislikes = models.ManyToManyField(User, related_name='post_dislikes')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    def teaser(self):
        return ' '.join(self.content.split()[:20]) + '...'
    
    def get_image_url(self):
        return self.image.url if self.image else None


class BlogImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    
    def __str__(self):
        return f"Image for {self.post.title}"
    
    
    
class SearchQuery(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

