# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_hero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='bage',
            new_name='hage',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='bsex',
            new_name='hsex',
        ),
    ]
