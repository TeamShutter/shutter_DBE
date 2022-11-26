
# Register your models here.
from django.contrib import admin

from studio.models import Place, Studio, Product, OpenedTime, Photographer, AssignedTime, StudioImage
# from studio.models import StudioTime, Time, StudioMerchandise, Merchandise
# Register your models here.
admin.site.register(Studio)
admin.site.register(Product)
admin.site.register(OpenedTime)
admin.site.register(Photographer)
admin.site.register(AssignedTime)
admin.site.register(Place)
admin.site.register(StudioImage)

# admin.site.register(StudioTime)
# admin.site.register(Time)
# admin.site.register(StudioMerchandise)
# admin.site.register(Merchandise)

