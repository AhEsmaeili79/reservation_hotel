# Generated by Django 5.1.5 on 2025-01-17 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='house_images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='house_images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='house_images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='house_images/'),
        ),
    ]
