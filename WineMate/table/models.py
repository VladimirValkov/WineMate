# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.db import models


class Assortment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assortment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Main(models.Model):
    id = models.AutoField(primary_key=True)
    id_category = models.PositiveIntegerField()
    id_vessel = models.PositiveIntegerField()
    id_assortment = models.PositiveIntegerField()
    date = models.DateTimeField()
    stage = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    num_protocol = models.CharField(max_length=50, blank=True, null=True)
    batch = models.CharField(max_length=50, blank=True, null=True)
    alcohol = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    sugar = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    titr_acids = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    ph = models.DecimalField(db_column='pH', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_acids = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    rel_weight = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    mal_acids = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    lactic_acids = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    total_ext = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    so2 = models.DecimalField(db_column='SO2', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    o2 = models.DecimalField(db_column='O2', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    co2 = models.DecimalField(db_column='CO2', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ntu = models.DecimalField(db_column='NTU', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    assim_nitrgen = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    pecto_test = models.CharField(max_length=1, blank=True, null=True)
    index_of_filt = models.IntegerField(blank=True, null=True)
    fe = models.DecimalField(db_column='Fe', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cu = models.DecimalField(db_column='Cu', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sowing = models.CharField(max_length=50, blank=True, null=True)
    sorb_acid = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    prot_stab = models.CharField(max_length=50, blank=True, null=True)
    delta = models.CharField(max_length=50, blank=True, null=True)
    cold_stab = models.CharField(max_length=50, blank=True, null=True)
    h2o2 = models.DecimalField(db_column='H2O2', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scheme = models.CharField(max_length=50, blank=True, null=True)
    other_proc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main'

    def __str__(self):
        return f'{self.id}'


class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'


class Vessel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'vessel'

class CellarModel(models.Model):
    date = models.Field()
    #id_vessel = models.Field()
    assort = models.Field()
    stage = models.Field()
    note = models.Field()
    alcohol = models.Field()
    sugar = models.Field()
    titr_acids = models.Field()
    pH = models.Field()
    vol_acids = models.Field()
    rel_weight = models.Field()
    mal_acids = models.Field()
    lactic_acids = models.Field()
    SO2 = models.Field()
    O2 = models.Field()
    CO2 = models.Field()
    NTU = models.Field()
    assim_nitrgen = models.Field()
    pecto_test = models.Field()


