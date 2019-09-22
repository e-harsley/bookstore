from django.db import models
from django.utils.html import escape, mark_safe
from django.utils.text import slugify
from django.conf import settings


class Category(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    category_cover = models.ImageField(upload_to='books/cover/%Y/%m/%d/',
                                       blank=True)
    color = models.CharField(max_length=7, default="E0FFFF")

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (
            color, name)
        return mark_safe(html)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Books(models.Model):

    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3

    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='book_create', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='book_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    book_cover = models.ImageField(upload_to='books/cover/%Y/%m/%d/',
                                   blank=False)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    author = models.CharField(max_length=250)
    about = models.TextField()
    publication_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    amazon_link = models.URLField(blank=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Books, self).save(*args, **kwargs)


class Review(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Books, related_name='book_review', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.user.username
