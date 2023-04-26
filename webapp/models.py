from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    """
    A model for storing vehicle information.

    Attributes:
            title (str): Vehicle title.
            door_count (int): number of doors in the car.
            seat_count (int): number of seats in the car.
            transmission (str): The type of vehicle gearbox.
                Must be from several options: "automatic" or "manual".
            rating (int): Vehicle rating from 0 to 5.
            price (int): Vehicle price.
            photo (PIL.Image): Photo of the car.
            is_main (bool): Flag indicating whether the photo is the main one.

    Methods:
            str(): returns the name of the vehicle as a string.
            get_absolute_url(): Returns the URL of the vehicle's detailed information page.
    """
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
        """
        Defines the Meta class with verbose names for the Car model.
        Attributes:
        verbose_name (str): A human-readable singular name for the model.
        verbose_name_plural (str): A human-readable plural name for the model.
        """
        verbose_name = "Car"
        verbose_name_plural = "Cars"
