import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book


# Create queries within functions

def show_all_authors_with_their_books():
    result = []
    for a in Author.objects.all().order_by('id'):
        books = Book.objects.filter(author=a)

        if not books:
            continue

        titles = ", ".join(b.title for b in books)
        result.append(f"{a.name} has written - {titles}!")
    return "\n".join(result)


def delete_all_authors_without_books():
    Author.objects.filter(books__isnull=True).delete()
