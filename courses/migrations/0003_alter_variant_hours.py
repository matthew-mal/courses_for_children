# Generated by Django 4.2 on 2023-04-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_variant_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='hours',
            field=models.IntegerField(verbose_name='Всего заданий'),
        ),
    ]
