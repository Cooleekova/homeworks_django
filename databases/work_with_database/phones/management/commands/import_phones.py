import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


# Написать скрипт для переноса данных из csv-файла в модель Phone.
# Скрипт необходимо разместить в файле import_phones.py в методе handle(self, *args, **options)

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                slug_name = slugify(line[1])
                phone = Phone.objects.create(
                    id=line[0],
                    name=line[1],
                    price=line[3],
                    image=line[2],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slug_name
                )
        return phone_reader

