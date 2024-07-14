from django.contrib import admin
from .models import Service, News, Faq, NewsImage, News_detail, Contact


class NewImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


admin.site.register(Service)
admin.site.register(News)
admin.site.register(Faq)
admin.site.register(NewsImage)
admin.site.register(News_detail)
admin.site.register(Contact)
