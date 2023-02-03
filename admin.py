from django.contrib import admin
from .models import Home, About_us, Category, Dish, Special, Events

admin.site.register(Home)

@admin.register(About_us)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo']


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [DishAdmin]

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'description', 'price', 'photo', 'category', 'is_special']
    list_filter = ['category', 'is_special', 'is_visible']
    list_editable = ['position', 'is_visible', 'price']

@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'description', 'photo']
    list_editable = ['position', 'is_visible', 'price']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'description', 'date', 'photo']
    list_filter = ['date']
    list_editable = ['position', 'is_visible']
