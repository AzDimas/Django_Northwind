from django.db import models

# Create your models here.

class USAEmployeePhoneBook(models.Model):
    full_name = models.CharField(primary_key=True, max_length=255)
    title_of_courtesy = models.CharField(max_length=50)
    home_phone = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'soal_pertama'

class TerritoriesWithAllEmployees(models.Model):
    territory_description = models.CharField(primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'soal_kedua'

class DepletedCategory(models.Model):
    category_name = models.CharField(primary_key=True, max_length=255)
    total_units_in_stock = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'soal_ketiga'

class FragileProducts(models.Model):
    product_name = models.CharField(primary_key=True, max_length=255)
    supplier_name = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    quantity_per_unit = models.TextField()
    units_in_stock = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'soal_keempat'

class EuropeanProductAveragePrice(models.Model):
    country = models.CharField(primary_key=True, max_length=255)
    average_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'soal_kelima'

class FavouriteShipper(models.Model):
    company_name = models.CharField(primary_key=True, max_length=255)
    total_orders = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'soal_keenam'

class TotalEmployeeInEveryRegion(models.Model):
    region_description = models.CharField(primary_key=True, max_length=255)
    total_employees = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'soal_ketujuh'

class GeneralPhoneBook(models.Model):
    full_name = models.CharField(primary_key=True, max_length=255)
    phone = models.IntegerField()
    entity_type = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'soal_kedelapan'