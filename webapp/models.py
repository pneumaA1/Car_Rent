from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ("automatic", "Automatic"),
        ("manual", "Manual")
    ]
    title = models.CharField(max_length=100)
    door_count = models.PositiveIntegerField()
    seats_count = models.PositiveIntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    rating = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='car_photos/', blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('webapp:car_detail', kwargs={'pk', self.pk})

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
