# Generated by Django 2.2.5 on 2019-09-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Reading',
        ),
    ]
