from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import re
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
DICTIONARY = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
              'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
              'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
              'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'cz',
              'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': 'b',
              'э': 'e', 'ю': 'yu', 'я': 'ya'}


def transliteration(title):
    text = str(title).lower()
    return re.sub(r'\w', lambda x: DICTIONARY.get(x.group(), x.group()), text)


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    description = models.CharField(max_length=512, verbose_name='Описание')
    post = models.TextField(verbose_name='Запись блога')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    autor = models.CharField(default='admin', max_length=64, verbose_name='Автор')
    slug = models.SlugField(default='', null=False,  db_index=True, unique=True, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        self.slug = slugify(transliteration(self.title))
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'slug': self.slug})
