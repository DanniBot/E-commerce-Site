# Generated by Django 3.2.5 on 2022-08-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
