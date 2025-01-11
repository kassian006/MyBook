from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField, ForeignKey
from phonenumber_field.modelfields import PhoneNumberField


STATUS_CHOICES = (
    ('pro', 'Pro'),
    ('simple', 'Simple')
)


class User(AbstractUser):
    age =models.PositiveSmallIntegerField(validators=[MinValueValidator(16),
                                                      MaxValueValidator(70)],
                                                      null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='Simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Author(models.Model):
    author_name = models.CharField(max_length=20)
    author_bio = models.TextField()
    author_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(80)],
                                                       null=True, blank=True)
    author_image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return f'{self.author_name}'


class Genre(models.Model):
    genre_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.genre_name}'


class Book(models.Model):
    book_name = models.CharField(max_length=32)
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    book_page = models.PositiveSmallIntegerField()
    description = models.TextField()
    book_image = models.ImageField(upload_to='book_image/')
    status_book = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.book_name}'

    def get_avg_rating(self):
        ratings = self.comments.all()
        if ratings.exists():
            return round(sum(i.stars for i in ratings) / ratings.count(), 1)
        return 0


class BookLanguages(models.Model):
    language_book = models.CharField(max_length=32)
    audio_book = models.FileField(upload_to='book_languages/')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_languages')

    def __str__(self):
        return self.language_book


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    stars = models.IntegerField(choices=[(i, str(i))for i in range(1, 11)], null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.book}'


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

class FavoriteBook(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Quote(models.Model):
    quote = CharField(max_length=200)
    book_quote = ForeignKey(Book, on_delete=models.CASCADE)
