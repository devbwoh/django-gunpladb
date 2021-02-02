from django.db import models


class Mechanic(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    armor = models.CharField(max_length=255, blank=True, null=True)
    height = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mechanic'


class Gunpla(models.Model):
    mechanic = models.ForeignKey('Mechanic', models.DO_NOTHING)
    grade = models.CharField(max_length=45)
    date = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    boxart = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gunpla'


class Image(models.Model):
    gunpla = models.ForeignKey(Gunpla, models.DO_NOTHING)
    filename = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'
