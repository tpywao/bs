from urllib.request import urlopen
from json import loads
from django.db import models


class Book(models.Model):
    url_base = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
    isbn = models.CharField(max_length=13, unique=True)
    stock = models.IntegerField('在庫数')
    title = models.CharField('タイトル', max_length=50, blank=True)
    author = models.CharField('著者', max_length=20, blank=True)
    published_date = models.DateField('発行日', blank=True)

    def save(self, *args, **kwargs):
        if not self.title or not self.author or self.published_date:
            response = urlopen(self.url_base + self.isbn)
            s = loads(response.read().decode('utf-8'))
            book_info = s['items'][0]['volumeInfo']
            if not self.title:
                self.title = book_info['title']
            if not self.author:
                self.author = book_info['authors'][0]
            if not self.published_date:
                self.published_date = book_info['publishedDate']
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = '書籍'
