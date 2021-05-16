from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices


# Данный фильтр даёт возможность фильтровать объявления по дате и статусу.
class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # https: // django - filter.readthedocs.io / en / latest / ref / filters.html

    created = DateFromToRangeFilter(field_name='created_at')
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
