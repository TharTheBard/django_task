from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Attribute(models.Model):
    název_atributu_id = models.IntegerField()
    hodnota_atributu_id = models.IntegerField()


class AttributeName(models.Model):
    název = models.CharField(max_length=50)
    kód = models.CharField(max_length=50)
    zobrazit = models.BooleanField(null=True, blank=True)


class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=50)


class Product(models.Model):
    název = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    cena = models.CharField(max_length=20)
    měna = models.CharField(max_length=10)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)


class ProductAttributes(models.Model):
    attribute = models.IntegerField()
    product = models.IntegerField()


class ProductImage(models.Model):
    product = models.IntegerField()
    obrázek_id = models.IntegerField()
    název = models.CharField(max_length=50)


class Image(models.Model):
    název = models.CharField(max_length=50)
    obrázek = models.CharField(max_length=500)


class Catalog(models.Model):
    název = models.CharField(max_length=50)
    obrázek_id = models.IntegerField(null=True, blank=True)
    products_ids = models.CharField(max_length=1000, validators=[validate_comma_separated_integer_list])
    attributes_ids = models.CharField(max_length=1000, validators=[validate_comma_separated_integer_list])
