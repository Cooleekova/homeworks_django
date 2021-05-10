from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    # переопределяем метод clean()
    def clean(self):
        # создаём переменную-счётчик
        main_scope_count = 0
        for form in self.forms:
            # проверяем значения is_main, если раздел помечен как главный,
            # увеличиваем счётчик на 1, если раздел не главный, счётчик не меняется
            check = form.cleaned_data.get('is_main')
            if check is True:
                main_scope_count += 1
        # если основных разделов выбрано больше, чем один,
        # то счётчик будет больше единицы и вызовется ошибка
        if main_scope_count > 1:
            raise ValidationError('Возможен только один основной раздел')
        # если ни один из разделов не выбран как основной,
        # то счётчик пустой и вызывается ошибка
        if main_scope_count == 0:
            raise ValidationError('Требуется выбрать основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
