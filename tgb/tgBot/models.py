from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)


class Profile(models.Model):
    referral_id = models.PositiveIntegerField(unique=True, validators=[
        MaxValueValidator(99999999),
        MinValueValidator(10000000)
    ])
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)

    def __str__(self):
        return self.user_name
