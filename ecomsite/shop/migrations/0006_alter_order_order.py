# Generated by Django 3.2.5 on 2022-08-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.CharField(default='', editable=False, max_length=10),
        ),
    ]