from django.db import models

from .fields import SliderField


class Stair(models.Model):
    title = models.CharField('Название лестницы', max_length=100)
    type_turn = models.ManyToManyField('Turn', blank=True, verbose_name='Варианты поворота')
    type_fence = models.ManyToManyField('Fence', blank=True, verbose_name='Варианты ограждений')
    type_track_support = models.ManyToManyField('TrackSupport', blank=True, verbose_name='Варианты пристенного профиля')
    material_stair = models.ManyToManyField('Material', blank=True, verbose_name='Доступные материалы')
    tint = models.ManyToManyField('Tint', blank=True, verbose_name='Варианты отделки')

    class Meta:
        verbose_name = 'Лестница'
        verbose_name_plural = 'Лестницы'

    def __str__(self):
        return self.title


class Range(models.Model):
    title = models.CharField(max_length=16)
    min = models.PositiveIntegerField(default=0)
    slider = SliderField()
    max = models.PositiveIntegerField(default=10000)
    step = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class HeightRange(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE)


class WidthMarsh(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE)


class MinWidthStep(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE)


class MinWidthTopStep(Range):
    stair = models.OneToOneField('Stair', on_delete=models.CASCADE)


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
