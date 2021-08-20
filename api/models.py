# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class People(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'people'


class Hosts(models.Model):
    host_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    domain = models.TextField(blank=True, null=True)
    ip_address = models.TextField(blank=True, null=True)
    mac_address = models.TextField(blank=True, null=True)
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'hosts'
# Unable to inspect table 'cd'
# The error was: cannot unpack non-iterable NoneType object
# Unable to inspect table '/Users/jbeimler/Projects/inspectdb_drf'
# The error was: cannot unpack non-iterable NoneType object
