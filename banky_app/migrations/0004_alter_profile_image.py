# Generated by Django 4.1 on 2023-03-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banky_app', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
