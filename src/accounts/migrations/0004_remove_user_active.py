# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 17:09


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
    ]