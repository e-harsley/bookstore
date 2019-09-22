from django import forms
from .models import Books, Review


class BookCreateForm(forms.ModelForm):

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Books
        fields = ('title', 'book_cover', 'author', 'about',
                  'publication_date', 'price', 'pages', 'amazon_link', 'book_type',
                  )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)
