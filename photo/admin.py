from django.contrib import admin


from photo.models import Like, Photo

# Register your models here.
admin.site.register(Photo)
admin.site.register(Like)