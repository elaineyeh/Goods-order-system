# Generated by Django 3.1.6 on 2021-02-17 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
    ]