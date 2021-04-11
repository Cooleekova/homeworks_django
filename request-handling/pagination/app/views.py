from django.shortcuts import render, redirect
from django.urls import reverse
import csv
import urllib.parse
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


stations_list = list()


def get_stations_list():
    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as file:
        reader = csv.DictReader(file)
        for row in reader:
            station_info = dict()
            station_info['Name'] = row['Name']
            station_info['Street'] = row['Street']
            station_info['District'] = row['District']
            stations_list.append(station_info)
    return stations_list


def bus_stations(request):
    get_stations_list()
    page_number = int(request.GET.get('page', 1))
    current_page = page_number
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)

    params_next = {'page': (page.next_page_number())}
    encoded_next = urllib.parse.urlencode(params_next)
    next_page_url = str(reverse('bus_stations') + '?' + encoded_next)
    previous = None
    if page.has_previous():
        params_prev = {'page': (page.previous_page_number())}
        encoded_prev = urllib.parse.urlencode(params_prev)
        previous = str(reverse('bus_stations') + '?' + encoded_prev)
    return render(request, 'index.html', context={
        'bus_stations': page.object_list,
        'current_page': current_page,
        'prev_page_url': previous,
        'next_page_url': next_page_url,
    })


