# Generated by Django 4.0 on 2022-01-30 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_bill_id_bill_alter_export_part_id_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='id_bill',
        ),
        migrations.RemoveField(
            model_name='export_part',
            name='id_bill',
        ),
        migrations.CreateModel(
            name='export_bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_bill', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web.bill')),
                ('part_all', models.ManyToManyField(blank=True, to='web.export_part')),
            ],
        ),
    ]
