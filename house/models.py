from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()

class House(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='house_images/')
    image2 = models.ImageField(upload_to='house_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='house_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='house_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='house_images/', null=True, blank=True)
    city = models.CharField(max_length=100)
    number_of_rooms = models.IntegerField()
    area = models.FloatField()
    number_of_parkings = models.IntegerField()
    capacity = models.IntegerField()
    price_per_day = models.IntegerField()
    pool = models.BooleanField(default=False)
    oven = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            img = img.resize((1000, 1000), Image.LANCZOS)
            img.save(img_path)


class Review(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('house', 'user')

    def __str__(self):
        return f'Review by {self.user.username} on {self.house.name}'