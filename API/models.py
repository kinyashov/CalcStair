from django.db import models


class Stair(models.Model):
    title = models.CharField('Название лестницы', max_length=100)
    min_height = models.PositiveIntegerField('Минимальная высота лестницы', default=600)
    max_height = models.PositiveIntegerField('Максимальная высота лестницы', default=3600)
    step_height = models.PositiveSmallIntegerField('Шаг высоты лестницы', default=5)
    min_marsh = models.PositiveIntegerField('Минимальная ширина марша', default=550)
    max_marsh = models.PositiveIntegerField('Максимальная ширина марша', default=1300)
    step_marsh = models.PositiveSmallIntegerField('Шаг ширины марша', default=5)
    type_turn = models.ManyToManyField('Turn', blank=True, verbose_name='Варианты поворота')
    min_width_step = models.PositiveIntegerField('Минимальная ширина ступени', default=100)
    max_width_step = models.PositiveIntegerField('Максимальная ширина ступени', default=350)
    step_width_step = models.PositiveSmallIntegerField('Шаг ширины ступени', default=5)
    min_width_top_step = models.PositiveIntegerField('Минимальная ширина верхней ступени', default=40)
    max_width_top_step = models.PositiveIntegerField('Максимальная ширина верхней ступени', default=300)
    step_width_top_step = models.PositiveSmallIntegerField('Шаг ширины верхней ступени', default=5)
    visible_first_marsh = models.BooleanField('Ограждение на первом марше', default=True)
    visible_invitation_step = models.BooleanField('Пригласительная ступень', default=True)
    type_fence = models.ManyToManyField('Fence', blank=True, verbose_name='Варианты ограждений')
    visible_riser = models.BooleanField('Подступенок', default=True)
    type_track_support = models.ManyToManyField('TrackSupport', blank=True, verbose_name='Варианты пристенного профиля')
    material_stair = models.ManyToManyField('Material', blank=True, verbose_name='Доступные материалы')
    tint = models.ManyToManyField('Tint', blank=True, verbose_name='Варианты отделки')
    patina = models.BooleanField('Патина', default=True)
    brush = models.BooleanField('Браш', default=True)

    class Meta:
        verbose_name = 'Лестница'
        verbose_name_plural = 'Лестницы'

    def __str__(self):
        return self.title


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
