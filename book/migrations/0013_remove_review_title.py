# Generated by Django 2.2.5 on 2019-09-22 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20190922_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
