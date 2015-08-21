# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_location_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
    ]
