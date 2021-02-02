# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Armament(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'armament'


class Boarding(models.Model):
    mechanic = models.ForeignKey('Mechanic', models.DO_NOTHING, primary_key=True)
    pilot = models.ForeignKey('Pilot', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'boarding'
        unique_together = (('mechanic', 'pilot'),)


class Equipment(models.Model):
    mechanic = models.ForeignKey('Mechanic', models.DO_NOTHING, primary_key=True)
    armaments = models.ForeignKey(Armament, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'equipment'
        unique_together = (('mechanic', 'armaments'),)


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


class Pilot(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pilot'
