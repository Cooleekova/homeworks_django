from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


# Реализуйте логику подсчета количества переходов с лендинга по GET параметру from-landing
def index(request):
    global counter_click
    from_landing = request.GET.get('from-landing')
    if from_landing:
        if from_landing == 'original':
            counter_click['original'] += 1
        if from_landing == 'test':
            counter_click['test'] += 1
        return render(request, 'index.html')
    if not from_landing:
        return render(request, 'index.html')


# ab_test_arg как GET параметр
def landing(request):
    global counter_show
    ab_test_arg = request.GET.get('ab-test-arg')
    if ab_test_arg == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    if ab_test_arg == 'test':
        counter_show['test'] += 1
        landing_page = 'landing_alternate.html'
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
        return render(request, landing_page)


def stats(request):
    global counter_click, counter_show
    try:
        original_conversion = counter_click['original'] / counter_show['original']
        test_conversion = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        original_conversion = "Переходов по ссылке original ещё не было"
        test_conversion = "Переходов по ссылке test ещё не было"
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
            'test_conversion': test_conversion,
            'original_conversion': original_conversion,
    })
