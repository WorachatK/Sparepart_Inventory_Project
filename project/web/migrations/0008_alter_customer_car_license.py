# Generated by Django 4.0 on 2022-01-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_customer_car_car_remove_customer_car_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_car',
            name='license',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
