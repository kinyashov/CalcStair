from django.db import models

from .fields import SliderField


class Stair(models.Model):
    title = models.CharField('Название лестницы', max_length=100)
    turns = models.ManyToManyField('Turn', blank=True, verbose_name='Варианты поворота')
    fences = models.ManyToManyField('Fence', blank=True, verbose_name='Варианты ограждений')
    track_supports = models.ManyToManyField('TrackSupport', blank=True, verbose_name='Варианты пристенного профиля')
    materials = models.ManyToManyField('Material', blank=True, verbose_name='Доступные материалы')
    tints = models.ManyToManyField('Tint', blank=True, verbose_name='Варианты отделки')

    class Meta:
        verbose_name = 'Лестница'
        verbose_name_plural = 'Лестницы'

    def __str__(self):
        return self.title


class Range(models.Model):

    # класс-родитель для всех полей с диапазонами,
    # для создания диапазона надо отнаследоваться от этого класса,
    # создать в admin.py форму для модели, указав родителем класс SliderInline
    # и добавить объект в функцию create_ranges
    min = models.PositiveIntegerField(default=0, verbose_name='минимальное значение')
    slider = SliderField(verbose_name='')
    max = models.PositiveIntegerField(default=10000, verbose_name='максимальное значение')
    step = models.PositiveSmallIntegerField(default=5, verbose_name='шаг диапазона')

    class Meta:
        abstract = True


class Height(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE, related_name='height')

    class Meta:
        verbose_name = 'Высота лестницы'
        verbose_name_plural = 'Высота лестницы'


class WidthMarsh(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE, related_name='width_marsh')

    class Meta:
        verbose_name = 'Ширина марша'
        verbose_name_plural = 'Ширина марша'


class MinWidthStep(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE, related_name='min_width_step')

    class Meta:
        verbose_name = 'Минимальная ширина ступени'
        verbose_name_plural = 'Минимальная ширина ступени'


class MinWidthTopStep(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE, related_name='min_width_top_step')

    class Meta:
        verbose_name = 'Минимальная ширина верхней ступени'
        verbose_name_plural = 'Минимальная ширина верхней ступени'


class Turn(models.Model):
    title = models.CharField('Название поворота', max_length=100)
    price = models.PositiveIntegerField('Цена поворота', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип поворота'
        verbose_name_plural = 'Типы поворотов'


class Fence(models.Model):
    title = models.CharField('Название ограждения/балюстрады', max_length=100)
    price = models.PositiveIntegerField('Цена ограждения/балюстрады', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип ограждения'
        verbose_name_plural = 'Типы ограждений'


class TrackSupport(models.Model):
    title = models.CharField('Название пристенного профиля', max_length=100)
    price = models.PositiveIntegerField('Цена пристенного профиля', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пристенный профиль'
        verbose_name_plural = 'Пристенные профили'


class Material(models.Model):
    title = models.CharField('Название материала', max_length=100)
    price = models.PositiveIntegerField('Цена метериала', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Tint(models.Model):
    title = models.CharField('Название отделки/тонировки', max_length=100)
    price = models.PositiveIntegerField('Цена отделки/тонировки', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Окраска/тонировка'
        verbose_name_plural = 'Окраска/тонировка'


# solution for inline-object in admin-site
# without this admin-site don't save unchanged inline-object
def create_ranges(sender, instance, created, **kwargs):
        if created:
            # TODO: сделать цикл, который бы сам подхватывал все ranges
            Height.objects.create(stair=instance)
            WidthMarsh.objects.create(stair=instance)
            MinWidthStep.objects.create(stair=instance)
            MinWidthTopStep.objects.create(stair=instance)


models.signals.post_save.connect(create_ranges, sender=Stair, weak=False,
                                 dispatch_uid='models.create_renges')