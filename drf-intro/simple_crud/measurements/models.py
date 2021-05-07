from django.db import models


class Project(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField(verbose_name='Объект')
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'Температура: {self.value}'

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
