from django.db import models
import uuid
import os

class Home(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='home/')

    def __str__(self):
        return f'{self.title}'


class About_us(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

    def __iter__(self):
        for item in self.dishes.all():
            yield item

class Dish(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip.split('.')[-1]
        file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('dishes/%Y-%m-%d/', file_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position',)


class Events(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip.split('.')[-1]
        file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join('events/%Y-%m-%d/', file_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-date', )
