from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Painting', 'Painting'),
        ('Photography', 'Photography'),
        ('Sculpture', 'Sculpture'),
        ('Digital Art', 'Digital Art'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    artist_name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100, blank=True)  
    medium = models.CharField(max_length=100, blank=True)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name