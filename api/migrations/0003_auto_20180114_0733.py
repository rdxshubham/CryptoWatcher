# Generated by Django 2.0.1 on 2018-01-14 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180114_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btc',
            old_name='date_b',
            new_name='date',
        ),
    ]
