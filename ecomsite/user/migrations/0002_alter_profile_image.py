# Generated by Django 3.2.5 on 2022-08-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_pic.webp', upload_to='photos'),
        ),
    ]
