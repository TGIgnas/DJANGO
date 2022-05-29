from django.db import models


class AutomobilioModelis(models.Model):
    markė = models.CharField('Markė', max_length=30, help_text='Įveskite automobilio markę')
    modelis = models.CharField('Modelis', max_length=30, help_text='Įveskite automobilio modelį')

    def __str__(self):
        return f'{self.markė} ({self.modelis})'

    class Meta:
        verbose_name = 'Automobilio Modelis'
        verbose_name_plural = 'Automobilio Modeliai'


class Automobilis(models.Model):
    automobilio_modelis = models.ForeignKey('AutomobilioModelis', on_delete=models.RESTRICT)
    valstybinis_nr = models.CharField('Valstybinis NR', max_length=30, help_text='Įveskite valstybinį numerį')
    vin_kodas = models.CharField('VIN kodas', max_length=30, help_text='Įveskite automobilio VIN kodą')
    klientas = models.CharField('Klientas', max_length=30, help_text='Įveskite kliento vardą')
    aprašymas = models.TextField('Aprašymas', max_length=2000, default='')

    def __str__(self):
        return f'{self.klientas} ({self.valstybinis_nr})'

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'


class Paslauga(models.Model):
    kaina = models.FloatField('Kaina')
    pavadinimas = models.CharField('Paslaugos pavadinimas', max_length=30, help_text='Įveskite paslaugos pavadinimą')

    def __str__(self):
        return f'{self.kaina} ({self.pavadinimas})'

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'


class Užsakymas(models.Model):
    automobilis = models.ForeignKey('Automobilis', on_delete=models.RESTRICT)
    data = models.DateField('Užsakymo data', max_length=30, help_text='Įveskite užsakymo datą')
    suma = models.FloatField('Suma', max_length=30, help_text='Įveskite užsakymo sumą')
    paslauga = models.ManyToManyField('Paslauga')

    def __str__(self):
        return f'{self.data} ({self.suma})({self.paslauga})'

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    STATUS = (
        ('p', 'Patvirtinta'),
        ('v', 'Vykdoma'),
        ('a', 'Atlikta'),
        ('t', 'Atšaukta'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='p',
        help_text='Statusas',
    )


class UžsakymoEilutė(models.Model):
    paslauga = models.ForeignKey('Paslauga', on_delete=models.RESTRICT)
    užsakymas = models.ForeignKey('Užsakymas', related_name='eilutes', on_delete=models.SET_NULL, null=True)
    kiekis = models.CharField('Kiekis', max_length=30, help_text='Įveskite kiekį')
    kaina = models.FloatField('Kaina', max_length=30, help_text='Įveskite užsakymo kainą')

    def __str__(self):
        return f'{self.paslauga})'

    class Meta:
        verbose_name = 'Užsakymo Eilutė'
        verbose_name_plural = 'Užsakymo Eilutės'