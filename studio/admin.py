
# Register your models here.
from django.contrib import admin

from studio.models import Studio, Product, OpenedTime, Photographer, AssignedTime

# Register your models here.
admin.site.register(Studio)
admin.site.register(Product)
admin.site.register(OpenedTime)
admin.site.register(Photographer)
admin.site.register(AssignedTime)

