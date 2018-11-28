# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ChannelData(models.Model):
    name = models.ForeignKey('Channels', models.DO_NOTHING, db_column='name')
    game = models.CharField(max_length=40)
    views = models.BigIntegerField()
    followers = models.BigIntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'channel_data'

    def __str__(self):
        output2 = str(self.views) + " " + self.game + " " + str(self.views)
        return output2

class Channels(models.Model):
    name = models.CharField(primary_key=True, max_length=25)
    sid = models.CharField(unique=True, max_length=20)
    bType = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'channels'

    def __str__(self):
        output = self.name
        return output

class SlugsData(models.Model):
    name = models.ForeignKey(Channels, models.DO_NOTHING, db_column='name')
    title = models.CharField(max_length=100)
    views = models.BigIntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    timestamp_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'slugs_data'
    
    def __str__(self):
        return self.name
