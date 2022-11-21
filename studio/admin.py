
# Register your models here.
from django.contrib import admin

from studio.models import Place, Studio, Product, OpenedTime, Photographer, AssignedTime, StudioImage

# Register your models here.
admin.site.register(Studio)
admin.site.register(Product)
admin.site.register(OpenedTime)
admin.site.register(Photographer)
admin.site.register(AssignedTime)
admin.site.register(Place)
admin.site.register(StudioImage)

