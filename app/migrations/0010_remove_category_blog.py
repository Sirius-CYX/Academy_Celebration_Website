# Generated by Django 4.1.2 on 2022-11-09 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_category_sort_name_delete_sort'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='blog',
        ),
    ]