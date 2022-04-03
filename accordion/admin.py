from django.contrib import admin
from .models import Post, User, Keyboard

# superuser username: monte
# email: monte@silver.io
# password: lolkkkkk
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Keyboard)
