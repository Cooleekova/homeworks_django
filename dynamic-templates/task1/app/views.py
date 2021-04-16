from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'app\inflation.html'
    with open('inflation_russia.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        context = {'inflation_data': reader}
        return render(request, template_name, context)
