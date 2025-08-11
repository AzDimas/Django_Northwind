from django.db import models
from django.contrib.auth.models import User, Permission

# ========================
# Role & Profile
# ========================
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    roles = models.ManyToManyField(Role, blank=True, related_name='profiles')

    def __str__(self):
        return f"{self.user.username}"

# ========================
# Report Models
# ========================
class USAEmployeePhoneBook(models.Model):
    full_name = models.CharField(primary_key=True, max_length=255)
    title_of_courtesy = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=50)  # 🔹 ubah dari IntegerField → CharField

    class Meta:
        managed = False
        db_table = 'soal_pertama'
        default_permissions = ()
        permissions = [
            ("view_usaemployeephonebook", "Can view USA Employee Phone Book"),
        ]

class TerritoriesWithAllEmployees(models.Model):
    territory_description = models.CharField(primary_key=True, max_length=255)
    full_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'soal_kedua'
        default_permissions = ()
        permissions = [
            ("view_territorieswithemployees", "Can view Territories With All Employees"),
        ]

class DepletedCategory(models.Model):
    category_name = models.CharField(primary_key=True, max_length=255)
    total_units_in_stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'soal_ketiga'
        default_permissions = ()
        permissions = [
            ("view_depletedcategory", "Can view Depleted Category"),
        ]

class FragileProducts(models.Model):
    product_name = models.CharField(primary_key=True, max_length=255)
    supplier_name = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    quantity_per_unit = models.CharField(max_length=255)  # 🔹 ubah TextField → CharField (lebih konsisten)
    units_in_stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'soal_keempat'
        default_permissions = ()
        permissions = [
            ("view_fragileproducts", "Can view Fragile Products"),
        ]

class EuropeanProductAveragePrice(models.Model):
    country = models.CharField(primary_key=True, max_length=255)
    average_unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'soal_kelima'
        default_permissions = ()
        permissions = [
            ("view_europeanproductaverageprice", "Can view European Product Average Price"),
        ]

class FavouriteShipper(models.Model):
    company_name = models.CharField(primary_key=True, max_length=255)
    total_orders = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'soal_keenam'
        default_permissions = ()
        permissions = [
            ("view_favouriteshipper", "Can view Favourite Shipper"),
        ]

class TotalEmployeeInEveryRegion(models.Model):
    region_description = models.CharField(primary_key=True, max_length=255)
    total_employees = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'soal_ketujuh'
        default_permissions = ()
        permissions = [
            ("view_totalemployeeineveryregion", "Can view Total Employee In Every Region"),
        ]

class GeneralPhoneBook(models.Model):
    full_name = models.CharField(primary_key=True, max_length=255)
    phone = models.CharField(max_length=50)  # 🔹 ubah dari IntegerField → CharField
    entity_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'soal_kedelapan'
        default_permissions = ()
        permissions = [
            ("view_generalphonebook", "Can view general phone book"),
        ]
