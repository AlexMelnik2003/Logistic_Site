from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),
                  path('about/', views.about, name='about'),
                  path('services/', views.services, name='services'),
                  path('contact/', views.contact, name='contact'),
                  path('news/', views.news, name='news'),
                  path('news/<int:news_id>/', views.news_detail, name='news_detail'),
                  path('faq/', views.faq_view, name='faq'),
                  path('faq_success/', views.faq_success, name='faq_success'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
