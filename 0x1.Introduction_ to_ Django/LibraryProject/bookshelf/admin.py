from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_year')  # Add 'id' to the list display
    search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)

