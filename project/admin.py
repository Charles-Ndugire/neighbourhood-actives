from django.contrib import admin
from .models import Neighbourhood,Business,Post,Announcements

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Announcements)
