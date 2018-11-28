# Generated by Django 2.1.3 on 2018-11-27 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lytics_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=40)),
                ('views', models.BigIntegerField()),
                ('followers', models.BigIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'channel_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SlugsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('views', models.BigIntegerField()),
                ('date_created', models.DateField()),
                ('time_created', models.TimeField()),
                ('timestamp_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'slugs_data',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='channels',
            options={'managed': False},
        ),
    ]