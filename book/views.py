from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import BookCreateForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here. create, read, update view and delete


@login_required
def book_create(request, id, slug):
    form = BookCreateForm(request.POST or None, request.FILES or None)
    category = get_object_or_404(Category, id=id, slug=slug)
    if form.is_valid():
        category_books = category.book_set.all()
        for s in category_books:
            if s.book_title == form.cleaned_data.get("book_title"):
                context = {
                    'category': category,
                    'form': form,
                    'messages.error': 'Error updating your profile',
                }
                return render(request, 'book/create_book.html', context)
        book = form.save(commit=False)
        book.user = request.user
        book.category = category
        book.save()
        return render(request, 'book/detail.html', {'category': category})

    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'book/create_book.html', context)

# @login_required
# def book_create(request, id, slug):
#     category = get_object_or_404(Category, id=id, slug=slug)
#     if request.method == 'POST':
#         form = BookCreateForm(data=request.POST)
#         if form.is_valid():
#             new_item = form.save(commit=False)
#             new_item.user = request.user
#             new_item.category = category
#             new_item.save()
#             messages.success(request, 'book added successfully')
#             return render(request, 'book/detail.html', {'category': category})
#         else:
#             messages.error(request, 'Error updating your profile')

#     else:
#         form = BookCreateForm()
#     return render(request, 'book/create_book.html', {'form': form})


@login_required
def categry_detail(request, slug, id):
    user = request.user
    category = get_object_or_404(Category, id=id, slug=slug)
    book = Books.objects.filter(category=category)
    read = Books.objects.filter(is_read=True, user=user)
    my_book = Books.objects.filter(category=category, user=user)
    if request.method == 'POST':
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.category = category
            new_item.save()
            messages.success(request, 'book added successfully')
            return redirect('book:category_detail', id=category.id, slug=category.slug)
        else:
            messages.error(request, 'Error updating your profile')

    else:
        form = BookCreateForm()
    return render(request, 'book/detail.html',
                  {'form': form, 'category': category, 'book': book, 'my_book': my_book, 'user': user, 'read': read})


@login_required
def book_detail(request, slug, id):
    book = get_object_or_404(Books, slug=slug, id=id)
    return render(request, 'book/book_detail.html', {'book': book})


@login_required
def index(request):
    category = Category.objects.all()
    return render(request, "book/index.html", {'category': category})


@login_required
def delete_book(request, category_id, book_id, slug):
    category = get_object_or_404(Category, id=category_id, slug=slug)
    book = Books.objects.get(pk=book_id)
    book.delete()
    messages.success(request, 'book deleted successfully')
    return redirect('book:category_detail', id=category.id, slug=category.slug)


@login_required
def read_book(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    try:
        if book.is_read:
            book.is_read = False
        else:
            book.is_read = True
        book.save()
    except (KeyError, Books.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


@login_required
def my_books(request, category_id):
    user = request.user
    category = get_object_or_404(Category, pk=category_id)
    book = Books.objects.filter(category=category, user=user)
    return render(request, 'book/mybook.html', {'category': category, 'book': book})


@login_required
def read_books(request, category_id):
    user = request.user
    book = Books.objects.filter(is_read=True, user=user)
    return render(request, 'book/read.html', {'book': book})


@login_required
def book_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    book = Books.objects.filter(category=category)
    return render(request, 'book/list.html', {'category': category, 'book': book})


# @login_required
# def reading_view(request, book_id):
#     form = BookForm()
#     context = {'form': form}
#     html_form = render_to_string('books/includes/partial_book_create.html',
#         context,
#         request=request,
#     )
#     return JsonResponse({'html_form': html_form})
#                   {'forms': forms, 'book': book, 'user': user})
