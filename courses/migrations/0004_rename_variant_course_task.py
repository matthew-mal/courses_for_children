# Generated by Django 4.2 on 2023-05-03 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_variant_hours'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variant',
            new_name='Course',
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
                ('hours', models.IntegerField(verbose_name='Всего заданий')),
                ('attached_file', models.FileField(upload_to='tasks/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]