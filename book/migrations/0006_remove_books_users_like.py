# Generated by Django 2.2.5 on 2019-09-19 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_books_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='users_like',
        ),
    ]
