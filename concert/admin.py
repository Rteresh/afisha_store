from django.contrib import admin
from concert.models import ClassicalMusic, OpenAir, Party, Basket
from users.models import User

# Register your models here.
admin.site.register(ClassicalMusic)
admin.site.register(OpenAir)
admin.site.register(Party)
admin.site.register(User)
admin.site.register(Basket)
