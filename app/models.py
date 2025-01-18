from django.db import models
from django.utils.text import slugify

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    shoot_type = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.shoot_type}"


class Portfolio(models.Model):
    title = models.CharField(max_length=255)  # Title like "Weddings"
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)  # Slug for URLs
    description = models.TextField(blank=True, null=True)  # Optional description
    cover_image = models.ImageField(upload_to='portfolio/covers/')  # Cover image for the portfolio

    def save(self, *args, **kwargs):
        # Automatically generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)  # Link to Portfolio
    image = models.ImageField(upload_to='portfolio/images/')  # Additional images

    def __str__(self):
        return f"Image for {self.portfolio.title}"
