# Generated by Django 2.2.5 on 2019-09-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('color', models.CharField(default='E0FFFF', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('author', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('publication_date', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('amazon_link', models.URLField(blank=True)),
                ('book_type', models.PositiveSmallIntegerField(choices=[(1, 'Hardcover'), (2, 'Paperback'), (3, 'E-book')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='book.Category')),
            ],
        ),
    ]