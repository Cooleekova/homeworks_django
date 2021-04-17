from django.db import models


class Phone(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.TextField()
        price = models.FloatField()
        image = models.TextField()
        release_date = models.DateField()
        lte_exists = models.BooleanField()
        slug = models.SlugField()

        def __str__(self):
                return f'{self.name}'

# В файле models.py нашего приложения создаем модель Phone
# с полями id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.
# Значение поля slug должно устанавливаться слагифицированным значением поля name.
