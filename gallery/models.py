from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    artist = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('Painting', 'Painting'), ('Sculpture', 'Sculpture')])
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.URLField(max_length=500)
    start_bid_time = models.DateTimeField()
    end_bid_time = models.DateTimeField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Bid(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.bid_amount}"

class Transaction(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.artwork.title} - {self.buyer.username}"
