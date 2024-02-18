from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, max_length=500)
    text = models.TextField()
    date = models.DateField()

    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-date'])
        ]

    def __str__(self):
        return self.name