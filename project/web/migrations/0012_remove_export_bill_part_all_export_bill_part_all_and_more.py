# Generated by Django 4.0 on 2022-02-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_export_part_id_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='export_bill',
            name='part_all',
        ),
        migrations.AddField(
            model_name='export_bill',
            name='part_all',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='export_part',
            name='id_bill',
            field=models.CharField(default='', max_length=40, null=True),
        ),
    ]
