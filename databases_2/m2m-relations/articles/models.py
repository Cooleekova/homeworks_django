from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    scopes = models.ManyToManyField(
        'Scope',
        verbose_name='Разделы',
        related_name='articles',
        through='ArticleScope'
    )


class Scope(models.Model):

    name = models.TextField(
        max_length=20,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    scope = models.ForeignKey(
        Scope,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Раздел',
    )

    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)
