# Generated by Django 4.0 on 2021-12-13 21:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('referral_id', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(10000000)])),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32)),
            ],
        ),
    ]
