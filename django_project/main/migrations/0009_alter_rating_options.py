# Generated by Django 5.1.3 on 2024-11-27 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_students_sex_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
    ]
