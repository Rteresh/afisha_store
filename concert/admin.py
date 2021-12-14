from django.contrib import admin
from concert.models import ClassicalMusic, OpenAir, Party, Basket
from users.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


# Register your models here.


@admin.register(ClassicalMusic)
class ClassicalMusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_tickets', 'type_of_voice', 'name_executor')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(OpenAir)
class OpenAirAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_tickets', 'address', 'headliner')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_tickets', 'age')
    ordering = ('name',)
    search_fields = ('name',)


class BasketAdminInLine(admin.TabularInline):
    model = Basket
    fields = ('concert', 'quantity_items_on_basket', 'created_timestamp', 'user')
    readonly_fields = ('created_timestamp',)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('concert', 'quantity_items_on_basket', 'created_timestamp', 'user')
    fields = ('concert', 'quantity_items_on_basket', 'created_timestamp', 'user')
    readonly_fields = ('created_timestamp',)
