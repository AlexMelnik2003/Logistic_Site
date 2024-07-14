from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, News, News_detail
from .forms import ContactForm, FaqForm


def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})


def about(request):
    return render(request, 'about.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохранение данных формы в модель Contact
            contact = form.save(commit=False)
            contact.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def news(request):
    news_list = News.objects.all()
    return render(request, 'news.html', {'news_list': news_list})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news_detail = get_object_or_404(News_detail, pk=news_id)  # Получаем детальную информацию о новости
    return render(request, 'news_detail.html', {'news': news, 'news_detail': news_detail})


def faq_view(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()
            return redirect('faq_success')
    else:
        form = FaqForm()
    return render(request, 'faq.html', {'form': form})


def faq_success(request):
    return render(request, 'faq_success.html')
