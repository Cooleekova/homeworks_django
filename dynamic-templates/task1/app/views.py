from django.shortcuts import render
import csv


data = list()


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста

    with open('inflation_russia.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            info = dict()
            info['Год'] = row['Год']
            info['Янв'] = row['Янв']
            info['Фев'] = row['Фев']
            info['Мар'] = row['Мар']
            info['Апр'] = row['Апр']
            info['Май'] = row['Май']
            info['Июн'] = row['Июн']
            info['Июл'] = row['Июл']
            info['Авг'] = row['Авг']
            info['Сен'] = row['Сен']
            info['Окт'] = row['Окт']
            info['Ноя'] = row['Ноя']
            info['Дек'] = row['Дек']
            info['Всего'] = row['Суммарная']
            data.append(info)

        my_dict = dict(reader)
        names = list(my_dict.keys())
        header = names[0:14]
    context = {'data': data, 'header': header}
    return render(request, template_name, context)
