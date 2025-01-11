from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookLanguages)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteBook)
admin.site.register(Quote)