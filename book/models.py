from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    title = models.CharField('title', max_length=200)
    price = models.IntegerField(default=1000)
    description = models.TextField('text')
    created_at = models.DateTimeField('date', default=timezone.now)

    def __str__(self):
        return self.title

class BuyingHistory(models.Model):
    book = models.ForeignKey(Book, verbose_name='book', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.PROTECT)
    is_sended = models.BooleanField('flag', default=False)
    stripe_id = models.CharField('title', max_length=200)
    created_at = models.DateTimeField('date',default=timezone.now)

    def __str__(self):
        return '{} {} {}'.format(self.book, self.user.email, self.is_sended)