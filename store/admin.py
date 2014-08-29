from django.contrib import admin
from store.models import Image, Logo, Manufacturer, Attribute, Price, Product


class ImageAdmin(admin.ModelAdmin):
	list_display = ('description', 'thumbnail')


class LogoAdmin(admin.ModelAdmin):
	list_display = ('description', 'thumbnail')


class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ('name', 'logo_thumb', 'is_linecard')


class PriceAdmin(admin.ModelAdmin):
	list_display = ('price', 'min_qty', 'max_qty')


class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_url": ("item_no",)}
	list_display = ('item_no', 'manu_no', 'thumbs', 'prices', 'weight')

admin.site.register(Image, ImageAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Attribute)
admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)