from django import template

register = template.Library()


@register.filter
def detectcolor(value):
    if value:
        value = float(value)
        if value <= 0.0:
            return "green"
        if value > 1:
            if 2 > value > 1:
                return "red lighten-3"
            if 5 > value > 2:
                return "red"
            if value > 5:
                return "red darken-3"








