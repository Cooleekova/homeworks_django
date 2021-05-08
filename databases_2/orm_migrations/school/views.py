from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    data = Student.objects.all().order_by('group').prefetch_related('teacher')
    school_info = list(data)
    context['object_list'] = school_info
    return render(request, template, context)
