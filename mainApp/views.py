from django.shortcuts import render
from datetime import datetime


# Create your views here.
def main_page(request):
    """
    Представление главной страницы сайта
    """
    title = "Небольшая страница с информацией обо мне!"
    surname = "Маликов"
    name = "Алексей"
    patronymic = "Валерьевич"
    birthday = datetime(2021, 3, 8)
    context = {
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'birthday': birthday,
        'title': title,
    }
    return render(request, 'index.html', context)


def study(request):
    """
    Представление страницы с информацией о местах обучения
    """
    title = "Мои места обучения"
    school_name = "Школа №1985"
    university = "Российский Новый Университет"
    context = {
        'title': title,
        'school_name': school_name,
        'university': university,

    }
    return render(request, 'study.html', context)


def work(request):
    """
    Представление страницы с информацией о местах работы
    """
    title = "Моя работа"
    employment_place = "Пятёрочка"
    post = "Кассир"
    context = {
        'title': title,
        'employment_place': employment_place,
        'post': post,
    }
    return render(request, 'work.html', context)
